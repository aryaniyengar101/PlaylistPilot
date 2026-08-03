from openai import OpenAI

from app.core.config import settings
from app.schemas.openai_schema import PlaylistRecommendations
from app.utils.logger import logger

client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


def generate_song_recommendations(
    mood: str,
    genre: str,
    activity: str,
    num_songs: int,
):

    logger.info("Calling OpenAI to generate song recommendations...")

    prompt = f"""
Generate exactly {num_songs} songs.

Mood: {mood}
Genre: {genre}
Activity: {activity}

Requirements:
- Songs must exist on Spotify.
- Match the requested mood.
- Match the requested activity.
- Avoid duplicate songs.
- Prefer well-known tracks unless the genre suggests otherwise.
- Return exactly {num_songs} songs.
"""

    try:

        response = client.responses.parse(
            model="gpt-5.5",
            input=prompt,
            text_format=PlaylistRecommendations,
        )

        songs = response.output_parsed.songs

        logger.info(
            f"OpenAI successfully generated {len(songs)} recommendations."
        )

        return songs

    except Exception as e:

        logger.exception("OpenAI playlist generation failed.")

        raise RuntimeError(
            "Failed to generate song recommendations."
        ) from e