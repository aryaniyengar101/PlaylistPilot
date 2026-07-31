from typing import List, Optional
from pydantic import BaseModel, Field


class PlaylistRequest(BaseModel):
    mood: str = Field(..., example="Energetic")
    genre: str = Field(..., example="Hip-Hop")
    activity: str = Field(..., example="Gym")
    num_songs: int = Field(..., gt=0, le=50, example=10)


class Song(BaseModel):
    title: str
    artist: str
    album: Optional[str] = None
    spotify_url: Optional[str] = None
    image_url: Optional[str] = None


class PlaylistResponse(BaseModel):
    playlist_name: str
    description: str
    songs: List[Song]