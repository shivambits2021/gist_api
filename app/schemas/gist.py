from pydantic import BaseModel, HttpUrl
from typing import Optional


class Gist(BaseModel):
    id: str
    html_url: HttpUrl
    description: Optional[str]
