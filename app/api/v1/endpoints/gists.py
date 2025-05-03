from fastapi import APIRouter, HTTPException
from app.services.get_gists import get_gists_from_user
from typing import List
from app.schemas.gist import Gist
from fastapi.params import Query

router = APIRouter()

@router.get("/{username}", response_model=List[Gist])
async def get_user_gists(username: str, page: int = Query(1, ge=1), per_page: int = Query(30, le=100)):
    try:
        gists = await get_gists_from_user(username, page=page, per_page=per_page)
        return gists
    except HTTPException as e:
        raise e
