from re import I
import socket

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

PORT = 30003
HOST = 'localhost'

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

    def update(self, msg):
        updated = False
        self.msg = msg
        if msg[10] and self.callsign != msg[10].replace(" ", ""):
            self.callsign = msg[10].replace(" ", "")
            updated = True
        if msg[11] and self.altitude != msg[11]:
            self.altitude = msg[11]
            updated = True
        if msg[12] and self.ground_speed != msg[12]:
            self.ground_speed = msg[12]
            updated = True
        if msg[14] and self.lat != msg[14]:
            self.lat = msg[14]
            updated = True
        if msg[15] and self.long != msg[15]:
            self.long = msg[15]
            updated = True
        if msg[16] and self.vertical_rate != msg[16]:
            self.vertical_rate = msg[16]
            updated = True
        if msg[17] and self.squawk != msg[17]:
            self.squawk = msg[17]
            updated = True
        return updated

    def __repr__(self):
        return f"Hex: {self.hex} Call:{self.callsign} Lat:{self.lat} Long:{self.long} Alt: {self.altitude} Spd: {self.ground_speed} Squawk: {self.squawk}"

def seperate_messages(message_string):
    decoded_string = message_string.decode('utf-8')
    return decoded_string.split('\r\n')

def parse_message_string(message_string):
    return message_string.split(',')

if __name__ == "__main__":
    aircrafts = []
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            message_string = s.recv(1024)
            message_array = seperate_messages(message_string)
            for split_message in message_array:
                updated = False
                parsed_message = parse_message_string(split_message)
                if not parsed_message or parsed_message == [''] or len(parsed_message) < 17:
                    continue
                ac = Aircraft(parsed_message)
                matching_ac = [aircraft for aircraft in aircrafts if aircraft.hex == ac.hex]
                if matching_ac:
                    updated = matching_ac[0].update(parsed_message)
                else:
                    aircrafts.append(ac)
                    updated = True
                if updated:
                    for ac in aircrafts:
                        print(ac)
