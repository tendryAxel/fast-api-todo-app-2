"""Main API routers."""
from fastapi import APIRouter

from .endpoints import crud_todo

router = APIRouter()
router.include_router(crud_todo.router, prefix="/todos", tags=["todos"])
