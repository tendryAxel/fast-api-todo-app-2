"""Test database."""
import importlib

from fastapi_todo_api import database


def test_database_url(monkeypatch):
    """Test database url."""
    monkeypatch.setattr("sqlmodel.create_engine", lambda *args, **kwargs: None)
    monkeypatch.setattr("fastapi_todo_api.database.settings.DB_DRIVER", "sqlite")
    monkeypatch.setattr("fastapi_todo_api.database.settings.DB_NAME", "data/db/test.sqlite3")
    importlib.reload(database)
    assert str(database.DATABASE_URL) == "sqlite:///data/db/test.sqlite3"

    monkeypatch.setattr("fastapi_todo_api.database.settings.DB_DRIVER", "postgresql+psycopg2")
    monkeypatch.setattr("fastapi_todo_api.database.settings.DB_NAME", "test")
    monkeypatch.setattr("fastapi_todo_api.database.settings.DB_USER", "test_user")
    monkeypatch.setattr("fastapi_todo_api.database.settings.DB_PASSWORD", "test_password")
    monkeypatch.setattr("fastapi_todo_api.database.settings.DB_HOST", "localhost")
    importlib.reload(database)
    assert str(database.DATABASE_URL) == "postgresql+psycopg2://test_user:***@localhost/test"
