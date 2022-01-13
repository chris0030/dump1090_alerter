import requests

class Pushover:
    def __init__(self, token, user_key, url):
        self.token = token,
        self.user_key = user_key,
        self.url = url

    def send_notification(self, message, photo_data=None):
        payload = {
            "token": self.token,
            "user": self.user_key,
            "message": message,
        }
        attachment = ("plane.jpg", photo_data, "image/jpeg")
        files = {"attachment": attachment} if photo_data else None 
        return requests.post(self.url, data=payload, files=files)