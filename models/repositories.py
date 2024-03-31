from pydantic import BaseModel, AnyHttpUrl
from database import Repository as RepositoryModel


class Repository(BaseModel):
    full_name: str
    html_url: AnyHttpUrl
    description: str | None = None

    def save(self):
        session = Session(engine)
