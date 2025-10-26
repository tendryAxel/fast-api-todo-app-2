"""Crud Todo endpoint."""
from typing import Sequence

from fastapi import APIRouter
from sqlmodel import select

from fastapi_todo_api.database import SessionDep
from fastapi_todo_api.models.todo_model import TodoModel

router = APIRouter()


@router.get("/")
def get_todos(session: SessionDep) -> Sequence[TodoModel]:
    """Return all todos."""
    todos = session.exec(select(TodoModel)).all()
    return todos
