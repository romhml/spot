from fastapi import APIRouter, HTTPException

from app.main import spotify

router = APIRouter()


@router.get("/")
async def get():
    return [{"name": "Item Foo"}, {"name": "item Bar"}]
