from fastapi import APIRouter
from app.api.v1.endpoints import gists

api_router = APIRouter()

api_router.include_router(gists.router, prefix="/user", tags=["gists"])

