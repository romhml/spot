from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security.oauth2 import OAuth2AuthorizationCodeBearer

from pydantic import BaseSettings
from typing import Optional

from app.managers.auth import SpotifyAuthManager


class Settings(BaseSettings):
    origins: list[str]
    spotify_client_secret: str
    spotify_client_id: str
    spotify_redirect_uri: str

    class Config:
        env_file = ".env"


settings = Settings()

app = FastAPI()

auth = SpotifyAuthManager(
    client_id=settings.spotify_client_id,
    client_secret=settings.spotify_client_secret,
    redirect_uri=settings.spotify_redirect_uri,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    pass


@app.on_event("shutdown")
async def shutdown_event():
    pass


from .routers import auth

app.include_router(auth.router, prefix="/auth")
