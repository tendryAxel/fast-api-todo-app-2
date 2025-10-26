"""Main module."""
import uvicorn
from fastapi import FastAPI
from fastapi_versionizer.versionizer import Versionizer

from . import database
from .api.routers import router

app = FastAPI(
    title="FastApi Todo Api",
    summary="Test my skill in fast api",
    contact={
        "name": "SourceCode GitHub repository",
        "url": "https://github.com/tendryAxel/fastapi-todo-api-2"
    },
)

app.include_router(router)

versions = Versionizer(
    app=app,
    prefix_format="/v{major}",
    semantic_version_format="{major}",
    latest_prefix="/latest",
    sort_routes=True
).versionize()


@app.get("/healthcheck", include_in_schema=True)
async def healthcheck() -> dict[str, str]:
    """Healthcheck endpoint."""
    return {"status": "ok"}


def main() -> None:
    """Main function."""
    uvicorn.run(app, host="0.0.0.0")  # nosec


if __name__ == "__main__":
    database.apply_migrations()
    main()
