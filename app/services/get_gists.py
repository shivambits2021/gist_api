from fastapi import HTTPException
from typing import List
import httpx
from app.schemas.gist import Gist
from app.core.config import settings
from app.core.logging_service.log_config import logger  

async def get_gists_from_user(username: str, page: int = 1, per_page: int = 30) -> List[Gist]:

    url = f"{settings.SOURCE_API_URL}/users/{username}/gists"
    
    params = {
        "page": page,
        "per_page": per_page,
    }

    logger.info(f"Fetching gists for user: {username} from URL: {url} with page: {page}, per_page: {per_page}")

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url, params=params)
        
        response.raise_for_status()

    except httpx.HTTPStatusError as http_err:
        logger.warning(f"GitHub API returned status {response.status_code} for user: {username} on page {page}")
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch gists.")
    except httpx.RequestError as req_err:
        logger.error(f"Request to GitHub failed: {req_err}")
        raise HTTPException(status_code=503, detail="External service unavailable.")
    except Exception as e:
        logger.exception(f"An unexpected error occurred while fetching gists for user {username}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error while fetching gists.")

    try:
        gists_data = response.json()
        if not gists_data:
            logger.info(f"No gists found for user: {username} on page {page}")
            return []  # No data, return empty list

        # Map the response data to the Gist schema
        gists = [Gist(**gist) for gist in gists_data]
        logger.info(f"Successfully fetched {len(gists)} gists for user: {username} on page {page}")
        return gists

    except Exception as parse_err:
        logger.exception(f"Failed to parse gist response for user: {username} on page {page}")
        raise HTTPException(status_code=500, detail="Internal server error while parsing gists.")
