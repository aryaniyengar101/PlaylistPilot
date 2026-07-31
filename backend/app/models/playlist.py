from sqlalchemy import Column, Integer, String
from app.database.database import Base, engine

from app.database.database import Base


class Playlist(Base):
    __tablename__ = "playlists"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)

    prompt = Column(String)

    mood = Column(String)

    songs = Column(String)