#/bin/sh

docker build -t fastapi-todo:cov --target cov .
docker run --rm -it fastapi-todo:cov
