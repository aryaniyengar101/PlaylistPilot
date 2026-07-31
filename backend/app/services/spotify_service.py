import os

from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()


client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")


sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret
    )
)


def search_track(title: str, artist: str):
    query = f"track:{title} artist:{artist}"

    results = sp.search(
        q=query,
        type="track",
        limit=1
    )

    items = results["tracks"]["items"]

    if not items:
        return None

    track = items[0]

    return {
        "title": track["name"],
        "artist": track["artists"][0]["name"],
        "album": track["album"]["name"],
        "spotify_url": track["external_urls"]["spotify"],
        "image_url": track["album"]["images"][0]["url"],
        "duration_ms": track["duration_ms"]
    }