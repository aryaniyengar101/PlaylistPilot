import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from app.core.config import settings
from app.utils.logger import logger


sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=settings.SPOTIFY_CLIENT_ID,
        client_secret=settings.SPOTIFY_CLIENT_SECRET,
    )
)


def search_track(title: str, artist: str):

    query = f"track:{title} artist:{artist}"

    logger.info(f"Searching Spotify: {title} - {artist}")

    try:

        results = sp.search(
            q=query,
            type="track",
            limit=1,
        )

        items = results["tracks"]["items"]

        if not items:

            logger.warning(
                f"Spotify couldn't find: {title} - {artist}"
            )

            return None

        track = items[0]

        logger.info(
            f"Spotify match found: {track['name']} - {track['artists'][0]['name']}"
        )

        return {
            "title": track["name"],
            "artist": track["artists"][0]["name"],
            "album": track["album"]["name"],
            "spotify_url": track["external_urls"]["spotify"],
            "image_url": track["album"]["images"][0]["url"],
            "duration_ms": track["duration_ms"],
        }

    except Exception as e:

        logger.exception(
            f"Spotify search failed for: {title} - {artist}"
        )

        return None