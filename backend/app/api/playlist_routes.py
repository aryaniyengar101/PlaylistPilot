from fastapi import APIRouter

from app.schemas.playlist_schema import (
    PlaylistRequest,
    PlaylistResponse,
)

from app.services.playlist_service import generate_playlist

router = APIRouter(
    prefix="/playlist",
    tags=["Playlist"]
)


@router.post(
    "/generate",
    response_model=PlaylistResponse
)
def create_playlist(data: PlaylistRequest):
    return generate_playlist(data)