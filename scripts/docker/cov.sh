#/bin/sh

docker build -t fastapi-todo:cov --target cov .
docker run --rm fastapi-todo:cov
