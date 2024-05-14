#! /bin/bash

mkdir -p ./dags ./logs ./plugins ./config
echo "AIRFLOW_UID=$(id -u)" >> .env

docker compose -f ./docker-compose.yaml up -d --build
