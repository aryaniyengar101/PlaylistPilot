from fastapi import FastAPI

from app.database.database import Base, engine
from app.models.playlist import Playlist

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="PlaylistPilot API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to PlaylistPilot 🚀"
    }