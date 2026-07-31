from app.schemas.playlist_schema import PlaylistRequest


def generate_playlist(data: PlaylistRequest):
    return {
        "playlist_name": f"{data.activity} {data.genre} Mix",
        "songs": [
            "Song 1",
            "Song 2",
            "Song 3",
            "Song 4",
            "Song 5"
        ]
    }