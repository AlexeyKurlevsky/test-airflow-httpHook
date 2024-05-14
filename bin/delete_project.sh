#! /bin/bash
docker compose -f ./docker-compose.yaml down -v

docker rmi $(docker images -a -q)
