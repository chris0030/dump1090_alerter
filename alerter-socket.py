from re import I
import socket
from hex_lookup import HEX_LOOKUP
from aircraft_code_lookup import AIRCRAFT_CODES
import os
from rich.live import Live
from rich.table import Table
from geopy.distance import geodesic
from datetime import datetime
from typeguard import typechecked
from typing import Optional

ALERTS = [
    {
        "field": "squawk",
        "comparison": "equal",
        "value": "7001",
    },
    {
        "field": "altitude",
        "comparison": "lt",
        "value": 500,
    },
    {
        "field": "model",
        "comparison": "equal",
        "value": "McDonnell Douglas F-15E Strike Eagle",
    }
]

FIELDS = [
    "message_type",
    "transmission_type",
    "session_id",
    "aircraft_id",
    "hex_ident",
    "flight_id",
    "date_msg_generated",
    "time_msg_generated",
    "date_message_logged",
    "time_message_logged",
    "callsign",
    "altitude",
    "ground_speed",
    "track",
    "lat",
    "long",
    "vertical_rate",
    "squawk",
    "alert",
    "emergency",
    "spi",
    "is_on_ground",
]

TABLE_HEADERS = [
    "Hex",
    "Callsign", 
    "Model",
    "Operator",
    "Lat",
    "Long",
    "Altitude",
    "Ground Speed",
    "Squawk",
    "Distance",
    "Last Seen",
    "Alerting"
]

PORT = 30003
HOST = 'localhost'
HOME_LAT = float(os.environ.get("HOME_LAT"))
HOME_LONG = float(os.environ.get("HOME_LONG"))

class Aircraft:
    def __init__(self, msg):
        self.msg = msg
        self.hex = msg[4]
        self.callsign = msg[10].replace(" ", "")
        self.altitude = msg[11]
        self.ground_speed = msg[12]
        self.lat = msg[14]
        self.long = msg[15]
        self.vertical_rate = msg[16]
        self.squawk = msg[17]
        self.model = HEX_LOOKUP.get(self.hex)
        self.operator = self.get_operator(AIRCRAFT_CODES)
        self.distance = self.get_distance(HOME_LAT, HOME_LONG)
        self.last_updated = datetime.now()

    def get_dict(self):
        return {
            "msg": self.msg,
            "hex": self.hex,
            "callsign": self.callsign,
            "altitude": self.altitude,
            "ground_speed": self.ground_speed,
            "lat": self.lat,
            "long": self.long,
            "vertical_rate": self.vertical_rate,
            "squawk": self.squawk,
            "model": self.model,
            "operator": self.operator,
            "distance": self.distance,
            "last_updated": self.last_updated,
        }

    def get_distance(self, home_lat: float, home_long: float) -> Optional[str]:
        if not home_lat or not home_long:
            return None
        if not self.lat or not self.long:
            return None
        distance = geodesic((self.lat, self.long), (home_lat, home_long)).kilometers
        return "{:.2f}".format(distance)

    def update(self, msg: list) -> bool:
        updated = False
        self.msg = msg
        if msg[10] and self.callsign != msg[10].replace(" ", ""):
            self.callsign = msg[10].replace(" ", "")
            self.operator = self.get_operator(AIRCRAFT_CODES)
            updated = True
        if msg[11] and self.altitude != msg[11]:
            self.altitude = msg[11]
            updated = True
        if msg[12] and self.ground_speed != msg[12]:
            self.ground_speed = msg[12]
            updated = True
        if msg[14] and self.lat != msg[14]:
            self.lat = msg[14]
            self.distance = self.get_distance()
            updated = True
        if msg[15] and self.long != msg[15]:
            self.long = msg[15]
            self.distance = self.get_distance(HOME_LAT, HOME_LONG)
            updated = True
        if msg[16] and self.vertical_rate != msg[16]:
            self.vertical_rate = msg[16]
            updated = True
        if msg[17] and self.squawk != msg[17]:
            self.squawk = msg[17]
            updated = True
        if updated:
            self.last_updated = datetime.now()
        return updated

    @typechecked
    def check_alerting(self, alerts: list) -> bool:
        for alert in alerts:
            if alert['comparison'] == "equal":
                value_to_check = self.get_dict()[alert['field']]
                if value_to_check == alert['value']:
                    return True
                return False
            elif alert['comparison'] == "lt":
                value_to_check = int(self.get_dict()[alert['field']])
                if value_to_check < alert['value']:
                    return True
                return False

    @typechecked
    def get_operator(self, ac_code_lookup: dict) -> str:
        return ac_code_lookup.get(self.callsign[0:3])

    @typechecked
    def seen_ago(self, now: datetime) -> int:
        time_delta = now - self.last_updated
        return int(time_delta.total_seconds())

    @typechecked
    def return_table_row(self) -> list:
        return [
            self.hex,
            self.callsign,
            self.model,
            self.operator,
            self.lat,
            self.long,
            self.altitude,
            self.ground_speed,
            self.squawk,
            self.distance,
            str(self.seen_ago(datetime.now())),
            self.check_alerting(ALERTS),
        ]

    @typechecked
    def __repr__(self) -> str:
        return ','.join(self.return_table_row())

@typechecked
def seperate_messages(message_string: bytes) -> list:
    decoded_string = message_string.decode('utf-8')
    return decoded_string.split('\r\n')

@typechecked
def parse_message_string(message_string: str) -> list:
    return message_string.split(',')

@typechecked
def generate_table(table_data: list) -> Table:
    table = Table()
    for header in TABLE_HEADERS:
        table.add_column(header)
    for dr in table_data:
        style = "indian_red" if dr[11] else "bright_white"
        table.add_row(
            dr[0],
            dr[1],
            dr[2],
            dr[3],
            dr[4],
            dr[5],
            dr[6],
            dr[7],
            dr[8],
            dr[9],
            dr[10],
            str(dr[11]),
            style=style
        )
    return table

@typechecked
def return_message_from_socket(host: str, port: int) -> Optional[bytes]:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
        except ConnectionRefusedError:
            print("Connection failed")
            return None
        message_string = s.recv(1024)
        return message_string

@typechecked
def parsed_message_valid(parsed_message: list) -> bool:
    if parsed_message and len(parsed_message) > 17:
        return True
    return False

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    clear_terminal()
    aircrafts = []
    with Live(generate_table([]), refresh_per_second=1) as live:
        while True:
            message_string = return_message_from_socket(HOST, PORT)
            if not message_string:
                print("Unable to connect to socket")
                exit()
            message_array = seperate_messages(message_string)
            for split_message in message_array:
                updated = False
                parsed_message = parse_message_string(split_message)
                if not parsed_message_valid(parsed_message):
                    continue
                ac = Aircraft(parsed_message)
                matching_ac = [aircraft for aircraft in aircrafts if aircraft.hex == ac.hex]
                if matching_ac:
                    updated = matching_ac[0].update(parsed_message)
                else:
                    aircrafts.append(ac)
                    updated = True
            table_data = []
            for ac in aircrafts:
                if ac.seen_ago(datetime.now()) < 60:
                    table_data.append(ac.return_table_row())
            live.update(generate_table(table_data))
