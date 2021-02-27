#!/usr/bin/env bash
docker ps -a -f status=exited
docker system prune -f
docker rmi tsundoku
docker build -t skill-mng-microservice .
docker run --detach --name skill-mng-microservice \
    -p 80:80 \
    -e "VIRTUAL_HOST=tsundoku.appsecurity.info" \
    -e "LETSENCRYPT_HOST=tsundoku.appsecurity.info" \
    -e "DATABASE_URL={}" \
    skill-mng-microservice
