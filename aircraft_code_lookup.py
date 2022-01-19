import json

with open('aircraft_codes.json') as json_file:
    AIRCRAFT_CODES = json.load(json_file)