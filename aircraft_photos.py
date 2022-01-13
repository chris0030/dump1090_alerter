import requests

class AircraftPhotos:
    def __init__(self, url):
        self.url = url
        self.headers = {"User-Agent": "Requests 1.0"}

    def get_photo_url(self, hex):
        photo_url = f"{self.url}{hex}"
        response = requests.get(photo_url, headers=self.headers)
        json_response = response.json()
        if not json_response.get('photos'):
            return None
        return json_response['photos'][0]['thumbnail']['src']
