"""The settings for our application."""
from functools import lru_cache

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Our settings class.
    This uses Pydantic's BaseSettings to define our settings.
    Pydantic's BaseSettings will read from environment variables.
    
    """
    app_name: str = "Time Service" # This will automatically read from the environment variable APP_NAME

# Sometimes settings might load from more than just local env variables.
# Its common to load from AWS Systems Manager Parameter Store for example.
# Implementing that is beyond this example.
# But that involves network calls, so lets make sure we only load our settings once, using lru_cache with maxsize=1
@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """
    Get our settings.
    """
    return Settings()
