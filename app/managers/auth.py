import requests

from pydantic import BaseModel

SPOTIFY_AUTH_URL = "https://accounts.spotify.com/api/token"


class SpotifyAuthManager(BaseModel):

    client_id: str
    client_secret: str
    redirect_uri: str

    def authenticate(self, code):
        body = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "authorization_code",
            "redirect_uri": self.redirect_uri,
            "code": code,
        }

        resp = requests.post(SPOTIFY_AUTH_URL, data=body)
        resp.raise_for_status()
        return resp.json()
