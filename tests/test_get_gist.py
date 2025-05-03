import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, AsyncMock
from fastapi import HTTPException
from app.main import app

client = TestClient(app)


# Test: GitHub API returns 500 error
@patch("app.api.v1.endpoints.gists.get_gists_from_user", new_callable=AsyncMock)
def test_get_user_gists_github_error(mock_get_gists):
    mock_get_gists.side_effect = HTTPException(status_code=500, detail="Failed to fetch gists.")

    response = client.get("/api/v1/user/octocat?page=1&per_page=2")

    assert response.status_code == 500
    assert response.json() == {"detail": "Failed to fetch gists."}
    mock_get_gists.assert_called_once_with("octocat", page=1, per_page=2)
