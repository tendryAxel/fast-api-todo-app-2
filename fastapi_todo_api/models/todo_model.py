"""Todo Model."""
from datetime import datetime

from sqlmodel import Field, SQLModel


class TodoModel(SQLModel, table=True):
    """Todo model representation for sql mapping."""
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str
    done: bool = Field(default=False)
    create_at: datetime = Field(default=datetime.now)
    update_at: datetime = Field(default=datetime.now)
