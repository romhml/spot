from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.main import auth


class AuthRequest(BaseModel):
    code: str


router = APIRouter()


@router.post("")
async def post(req: AuthRequest):
    return auth.authenticate(req.code)
