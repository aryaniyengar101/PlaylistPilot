from pydantic import BaseModel, Field


class PlaylistRequest(BaseModel):
    mood: str = Field(..., example="Happy")
    genre: str = Field(..., example="Pop")
    activity: str = Field(..., example="Workout")
    num_songs: int = Field(..., gt=0, le=50, example=10)


class PlaylistResponse(BaseModel):
    playlist_name: str
    songs: list[str]