from openai import OpenAI

from app.core.config import settings
from app.schemas.openai_schema import PlaylistRecommendations

client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


def generate_song_recommendations(mood, genre, activity, num_songs):

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
- Return only the requested schema.
"""

    response = client.responses.parse(
        model="gpt-5.5",
        input=prompt,
        text_format=PlaylistRecommendations,
    )

    return response.output_parsed.songs