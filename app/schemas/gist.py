from pydantic import BaseModel, HttpUrl
from typing import Optional, Dict


class GistFile(BaseModel):
    filename: str
    type: str
    language: Optional[str]
    raw_url: HttpUrl
    size: int


class GistOwner(BaseModel):
    login: str
    id: int
    node_id: str
    avatar_url: HttpUrl
    gravatar_id: str
    url: HttpUrl
    html_url: HttpUrl
    followers_url: HttpUrl
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: HttpUrl
    organizations_url: HttpUrl
    repos_url: HttpUrl
    events_url: str
    received_events_url: HttpUrl
    type: str
    user_view_type: Optional[str]
    site_admin: bool


class Gist(BaseModel):
    url: HttpUrl
    forks_url: HttpUrl
    commits_url: HttpUrl
    id: str
    node_id: str
    git_pull_url: HttpUrl
    git_push_url: HttpUrl
    html_url: HttpUrl
    files: Dict[str, GistFile]
    public: bool
    created_at: str
    updated_at: str
    description: Optional[str]
    comments: int
    user: Optional[dict]
    comments_enabled: bool
    comments_url: HttpUrl
    owner: GistOwner
    truncated: bool
