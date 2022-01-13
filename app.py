import json
import time
import requests
import pprint
from bounding_box import BoundingBox
from pushover import Pushover
from config import *

def get_aircraft_photo(hex):
    headers = {"User-Agent": "Requests 1.0"}
    response = requests.get(PS_URL + hex, headers=headers)
    json_response = response.json()
    if not json_response.get('photos'):
        return None
    return json_response['photos'][0]['thumbnail']['src']

def load_json_file(path):
    with open(path, 'r') as file:
        json_file = json.load(file)
    return json_file

def parse_json_from_file(json_file):
    return json_file.get('aircraft')

def check_squawk_from_ac(aircraft, squawk_code):
    squawk = aircraft.get('squawk')
    return squawk == squawk_code

def get_alt_from_ac(aircraft):
    altitude = aircraft.get('alt_baro')
    if not altitude:
        altitude = aircraft.get('alt_geom')
    if not altitude:
        altitude = aircraft.get('nav_altitude_mcp')
    if not altitude:
        return None
    return altitude


def check_alt_from_ac(altitude, check_altitude, under=True):
    if not altitude:
        return False
    if under:
        return altitude < check_altitude
    else:
        return altitude > check_altitude

if __name__ == '__main__':
    pp = pprint.PrettyPrinter(indent=2)
    bounding_box = BoundingBox(
        BB_UPPER_LAT,
        BB_LOWER_LAT,
        BB_UPPER_LON,
        BB_LOWER_LON
    )
    pushover = Pushover(
        PUSHOVER_TOKEN,
        PUSHOVER_USER_KEY,
        PUSHOVER_URL,
    )
    pushover.send_notification("Starting alerter")
    while True:
        json_file = load_json_file(AIRCRAFT_JSON)
        ac_list = parse_json_from_file(json_file)
        for ac in ac_list:
            altitude = get_alt_from_ac(ac)
            squawk_check = check_squawk_from_ac(ac, "7001")
            alt_check = check_alt_from_ac(altitude, 2000)
            bounding_check = bounding_box.check_bounding(
                ac.get('lat'),
                ac.get('lon')
            )
            alert = (squawk_check or alt_check) and bounding_check
            if alert:
                message = f"Aircraft alerting: Flight: {ac.get('flight')} - Alt {altitude} - Squawk: {ac.get('squawk')}"
                pp.pprint(message)
                hex = ac.get('hex')
                photo = get_aircraft_photo(hex) if hex else None
                if photo:
                    response = requests.get(photo.replace("\\", ""))
                    photo_data = response.content
                else:
                    photo_data = None
                pushover.send_notification(message, photo_data)
                time.sleep(15)