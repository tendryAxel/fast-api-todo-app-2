#/bin/sh

docker build -t fastapi-todo:test --target test .
docker run --rm fastapi-todo:test
