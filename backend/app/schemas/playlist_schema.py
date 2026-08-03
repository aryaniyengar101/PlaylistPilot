from pydantic import BaseModel, Field, field_validator


class PlaylistRequest(BaseModel):

    mood: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Desired mood",
    )

    genre: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Music genre",
    )

    activity: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Activity",
    )

    num_songs: int = Field(
        default=10,
        ge=1,
        le=30,
        description="Number of songs (1-30)",
    )

    @field_validator("mood", "genre", "activity")
    @classmethod
    def validate_strings(cls, value: str):

        value = value.strip()

        if not value:
            raise ValueError("Field cannot be empty.")

        return value


class Song(BaseModel):

    title: str
    artist: str
    album: str
    spotify_url: str
    image_url: str


class PlaylistResponse(BaseModel):

    playlist_name: str
    description: str
    songs: list[Song]