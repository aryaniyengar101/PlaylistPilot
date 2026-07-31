from app.schemas.playlist_schema import (
    PlaylistRequest,
    Song
)

from app.services.spotify_service import search_track


def generate_playlist(data: PlaylistRequest):

    requested_songs = [
        ("Till I Collapse", "Eminem"),
        ("POWER", "Kanye West"),
        ("Stronger", "Kanye West"),
        ("Industry Baby", "Lil Nas X"),
        ("Remember The Name", "Fort Minor"),
    ]

    songs = []

    for title, artist in requested_songs[:data.num_songs]:

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

    return {
        "playlist_name": f"{data.activity} {data.genre} Mix",
        "description": f"A {data.mood.lower()} playlist for {data.activity.lower()}.",
        "songs": songs,
    }