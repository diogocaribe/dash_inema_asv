from pydantic_settings import BaseSettings, SettingsConfigDict

import sys
import os

# Adiciona o diretório raiz ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8', extra='ignore'
    )

    DATABASE: str
    USER_DB: str
    PASSWORD_DB: str
    HOST: str
    PORT: int

    DATABASE_URL: str
