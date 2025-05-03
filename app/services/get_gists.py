from fastapi import HTTPException
from typing import List
import httpx
from app.schemas.gist import Gist

async def get_gists_from_user(username: str) -> List[Gist]:
    url = f"https://api.github.com/users/{username}/gists"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch gists.")
    gists_data = response.json()
    return [Gist(**gist) for gist in gists_data]