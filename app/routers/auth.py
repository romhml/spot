from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.main import auth


class AuthRequest(BaseModel):
    code: str


class RefreshRequest(BaseModel):
    refresh_token: str


router = APIRouter()


@router.post("")
async def post(req: AuthRequest):
    return auth.authenticate(req.code)


@router.post("/refresh")
async def refresh(req: RefreshRequest):
    return auth.refresh(req.refresh_token)
