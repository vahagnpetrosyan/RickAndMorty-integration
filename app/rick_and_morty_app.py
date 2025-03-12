import os
import json

from fastapi import FastAPI, Depends
from .rm_client import RickAndMortyClient
from .settings import Settings

class RickAndMortyApp:
    def __init__(self):
        
        self._app = FastAPI(
            title="Rick & Morty Data Service (Class-Based w/ separate file)"
        )
        self.settings = Settings()
        self.settings.DATA_DIR = "data"
        os.makedirs(self.settings.DATA_DIR, exist_ok=True)
        self.setup_routes()

    def get_app(self) -> FastAPI:
        return self._app

    def get_rick_and_morty_client(self) -> RickAndMortyClient:
        return RickAndMortyClient(base_url=self.settings.RICKMORTY_BASE_URL)

    def setup_routes(self):
        @self._app.get("/characters")
        async def get_characters(
            client: RickAndMortyClient = Depends(self.get_rick_and_morty_client)
        ):
            characters = await client.fetch_all_characters()
            file_path = os.path.join(self.settings.DATA_DIR, "characters.json")
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(characters, f, indent=2)
            return characters

        @self._app.get("/locations")
        async def get_locations(
            client: RickAndMortyClient = Depends(self.get_rick_and_morty_client)
        ):
            locations = await client.fetch_all_locations()
            file_path = os.path.join(self.settings.DATA_DIR, "locations.json")
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(locations, f, indent=2)
            return locations

        @self._app.get("/episodes")
        async def get_episodes(
            client: RickAndMortyClient = Depends(self.get_rick_and_morty_client)
        ):
            episodes = await client.fetch_all_episodes()
            file_path = os.path.join(self.settings.DATA_DIR, "episodes.json")
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(episodes, f, indent=2)
            return episodes

        @self._app.get("/health")
        async def health_check():
            return {"status": "ok"}
