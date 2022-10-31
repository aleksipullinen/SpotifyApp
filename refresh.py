from salasanat import refreshToken, base_64
import requests
import json

class Refresh:
    def __init__(self):
        self.refreshToken = refreshToken
        self.base_64 = base_64

    def refresh(self):

        query = "https://accounts.spotify.com/api/token"
        response = requests.post(query,
                data={"grant_type": "refresh_token", 
                "refresh_token": refreshToken},
                headers={"Authorization": "Basic " + base_64})

        response = response.json()

        return response["access_token"]

        