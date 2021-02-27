#!/usr/bin/env bash
docker ps -a -f status=exited
docker system prune -f
docker rmi cloudcr-skill-mng
docker build -t cloudcr-skill-mng .
