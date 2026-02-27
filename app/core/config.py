try:
    from pydantic_settings import BaseSettings
except ImportError:
    from pydantic import BaseSettings

class Settings(BaseSettings):
    OPENROUTER_API_KEY: str
    OPENROUTER_MODEL: str
    OPENAI_EMBED_MODEL: str
    QDRANT_URL: str
    QDRANT_COLLECTION: str

    class Config:
        env_file = ".env"

settings = Settings()
