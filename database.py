from pydantic import AnyHttpUrl
from sqlmodel import Field, SQLModel, create_engine


class Repository(SQLModel, table=True):
    full_name: int | None = Field(default=None, primary_key=True)
    html_url: AnyHttpUrl
    description: str | None = None


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

SQLModel.metadata.create_all(engine)