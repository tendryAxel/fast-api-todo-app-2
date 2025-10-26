#/bin/sh

docker build -t fastapi-todo:test --target test .
docker run --rm -it fastapi-todo:test
