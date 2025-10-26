FROM python:3.10-alpine

LABEL maintainer="tendryAxel"
LABEL description="Test my skill in fast api"
LABEL org.opencontainers.image.authors="tendryAxel"
LABEL org.opencontainers.image.title="FastApi Todo Api"
LABEL org.opencontainers.image.description="Test my skill in fast api"
LABEL org.opencontainers.image.source="https://github.com/tendryAxel/fastapi-todo-api-2"
LABEL org.opencontainers.image.licenses="None"
LABEL org.opencontainers.image.base.name="docker.io/library/python:3.10-alpine"

WORKDIR /app
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN apk update && \
    rm -rf /var/cache/apk/* && \
    pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock /app/
RUN poetry install --only main --no-dev --no-root --no-interaction --no-ansi

COPY . /app/

EXPOSE 8000
CMD ["poetry", "run", "python", "-m", "fastapi_todo_api.main"]
