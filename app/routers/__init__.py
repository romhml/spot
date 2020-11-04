from fastapi import Header, HTTPException
from typing import Optional


async def authorize(authorization: Optional[str] = Header(None)):
    if authorization == None:
        raise HTTPException(status_code=401)

    scheme, _, token = authorization.partition(" ")
    if scheme != "Bearer" or token == None:
        raise HTTPException(status_code=400)
    return None
