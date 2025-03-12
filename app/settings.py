from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    RICKMORTY_BASE_URL: str = "https://rickandmortyapi.com/api"
    DATA_DIR: str = "data"