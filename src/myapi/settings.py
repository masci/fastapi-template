import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Configure the app, whenever possible the values should be
    overridable through environment variables.
    """
    debug: bool = os.environ.get('DEBUG', False)
