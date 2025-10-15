from functools import lru_cache
import os
from pydantic_settings import BaseSettings


class EnvironmentSettings(BaseSettings):
    API_VERSION: str
    APP_NAME: str
    DEBUG_MODE: bool
    AZURE_KEYVAULT_URL: str
    URL_POST: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_environment_variables():
    return EnvironmentSettings()