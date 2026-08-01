from app.schemas.playlist_schema import PlaylistRequest
from app.services.openai_service import generate_song_recommendations


def get_song_recommendations(data: PlaylistRequest):

    songs = generate_song_recommendations(
        mood=data.mood,
        genre=data.genre,
        activity=data.activity,
        num_songs=data.num_songs,
    )

    return [
    (song.title, song.artist)
    for song in songs
]
    