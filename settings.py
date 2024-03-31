import pathlib

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    pem_file_location: pathlib.Path
    app_id: str


settings = Settings()