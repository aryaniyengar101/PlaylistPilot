from fastapi import APIRouter, HTTPException

from app.schemas.playlist_schema import (
    PlaylistRequest,
    PlaylistResponse,
)
from app.services.playlist_service import generate_playlist
from app.utils.logger import logger

router = APIRouter(
    prefix="/playlist",
    tags=["Playlist"],
)


@router.post(
    "/generate",
    response_model=PlaylistResponse,
)
def create_playlist(data: PlaylistRequest):

    try:

        return generate_playlist(data)

    except RuntimeError as e:

        logger.exception("Playlist generation failed.")

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )

    except Exception:

        logger.exception("Unexpected server error.")

        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred.",
        )