from app.schemas.playlist_schema import (
    PlaylistRequest,
    PlaylistResponse,
    Song,
)

from app.services.ai_service import get_song_recommendations
from app.services.spotify_service import search_track


def generate_playlist(data: PlaylistRequest) -> PlaylistResponse:

    recommended_songs = get_song_recommendations(data)

    songs = []

    for title, artist in recommended_songs:

        spotify_data = search_track(title, artist)

        if spotify_data:

            songs.append(
                Song(
                    title=spotify_data["title"],
                    artist=spotify_data["artist"],
                    album=spotify_data["album"],
                    spotify_url=spotify_data["spotify_url"],
                    image_url=spotify_data["image_url"],
                )
            )

    return PlaylistResponse(
        playlist_name=f"{data.activity} {data.genre} Mix",
        description=f"A {data.mood.lower()} playlist for {data.activity.lower()}.",
        songs=songs,
    )