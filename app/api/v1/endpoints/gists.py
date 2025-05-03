from fastapi import APIRouter
from app.services.get_gists import get_gists_from_user
from typing import List
from app.schemas.gist import Gist



router = APIRouter()

@router.get("/users/{username}/gists", response_model=List[Gist])
async def get_user_gists(username: str):
    return await get_gists_from_user(username)

