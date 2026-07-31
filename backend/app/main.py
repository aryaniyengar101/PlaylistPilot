from fastapi import FastAPI

from app.database.database import Base, engine
from app.models.playlist import Playlist

# Import the playlist router
from app.api.playlist_routes import router as playlist_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="PlaylistPilot API",
    version="1.0.0"
)

# Register the router
app.include_router(playlist_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to PlaylistPilot 🚀"
    }