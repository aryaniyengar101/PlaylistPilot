from pydantic import BaseModel


class SongRecommendation(BaseModel):
    title: str
    artist: str


class PlaylistRecommendations(BaseModel):
    songs: list[SongRecommendation]