class BoundingBox:
    def __init__(self, upper_lat, lower_lat, upper_lon, lower_lon):
        self.upper_lat = upper_lat
        self.lower_lat = lower_lat
        self.upper_lon = upper_lon
        self.lower_lon = lower_lon

    def _is_between(self, check_value, upper_value, lower_value):
        if check_value < upper_value and check_value > lower_value:
            return True
        return False

    def check_bounding(self, lat, lon):
        lat_bounding = self._is_between(lat, self.upper_lat, self.lower_lat)
        lon_bounding = self._is_between(lon, self.upper_lon, self.lower_lon)
        return lat_bounding and lon_bounding