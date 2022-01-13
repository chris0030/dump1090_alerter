import unittest
from app import (
    get_aircraft_photo,
    load_json_file,
    parse_json_from_file,
    check_squawk_from_ac,
    get_alt_from_ac,
    check_alt_from_ac,
)
from bounding_box import BoundingBox
from pushover import Pushover
from test_aircraft import test_aircraft_json
from config import *

class TestApp(unittest.TestCase):

    def test_get_aircraft_photo(self):
        url = get_aircraft_photo("43C2B5")
        assert url == "https://cdn.planespotters.net/34417/zz419-royal-air-force-hawker-beechcraft-350cer-shadow-r1-b300c_PlanespottersNet_578211_c0d291f1e8_t.jpg"

    def test_send_push_notification(self):
        pushover = Pushover(
            PUSHOVER_TOKEN,
            PUSHOVER_USER_KEY,
            PUSHOVER_URL,
        )
        notification = pushover.send_notification("Testing alerter")
        assert notification.status_code == 200

    def test_load_json_file(self):
        json_file = load_json_file("test_aircraft.json")
        assert json_file == test_aircraft_json

    def test_parse_json_from_file(self):
        ac_list = parse_json_from_file(load_json_file("test_aircraft.json"))
        assert ac_list == test_aircraft_json['aircraft']

    def test_check_squawk_from_ac(self):
        ac = test_aircraft_json['aircraft'][0]
        squawk_check = check_squawk_from_ac(ac, "6302")
        assert squawk_check

    def test_check_squawk_false_from_ac(self):
        ac = test_aircraft_json['aircraft'][0]
        squawk_check = check_squawk_from_ac(ac, "7001")
        assert not squawk_check

    def test_get_alt_from_ac_under(self):
        alt = check_alt_from_ac(10000, 15000)
        assert alt

    def test_get_alt_from_ac_under_false(self):
        alt = check_alt_from_ac(15000, 10000)
        assert not alt

    def test_get_alt_from_ac_over(self):
        alt = check_alt_from_ac(15000, 10000, False)
        assert alt

    def test_get_alt_from_ac_over_false(self):
        alt = check_alt_from_ac(10000, 15000, False)
        assert not alt

    def test_get_alt_from_ac_baro(self):
        ac = test_aircraft_json['aircraft'][0]
        alt = get_alt_from_ac(ac)
        assert alt == 41025
    
    def test_get_alt_from_ac_geom(self):
        ac = test_aircraft_json['aircraft'][1]
        alt = get_alt_from_ac(ac)
        assert alt == 25050

    def test_bounding_box_check_bounding(self):
        bounding_box = BoundingBox(
            BB_UPPER_LAT, 
            BB_LOWER_LAT, 
            BB_UPPER_LON, 
            BB_LOWER_LON
        )
        lat = 53.197292
        long = -3.824530
        bounding_check = bounding_box.check_bounding(lat, long)
        assert bounding_check

    def test_bounding_box_check_bounding(self):
        bounding_box = BoundingBox(
            BB_UPPER_LAT, 
            BB_LOWER_LAT, 
            BB_UPPER_LON, 
            BB_LOWER_LON
        )
        lat = 53.136473
        long = -3.994560
        bounding_check = bounding_box.check_bounding(lat, long)
        assert not bounding_check

if __name__ == "__main__":
    unittest.main()