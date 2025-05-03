from fastapi import FastAPI
from app.api.v1.endpoints import api_router
app = FastAPI(
    title="GitHub Gist API",
    description="An API to interact with GitHub Gists",
    version="1.0.0"
)


app.include_router(api_router, prefix="/api/v1")
