from fastapi import Depends, FastAPI, Header, HTTPException
from pydantic import BaseSettings
from typing import Optional

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class Settings(BaseSettings):
    spotify_client_secret: str
    spotify_client_id: str

    class Config:
        env_file = ".env"


settings = Settings()

spotify = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=settings.spotify_client_id,
        client_secret=settings.spotify_client_secret,
    )
)

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    pass


@app.on_event("shutdown")
async def shutdown_event():
    pass


from .routers import player

app.include_router(player.router)
