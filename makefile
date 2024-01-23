#!makefile
COMPOSE_FILE_SERVICES="./etc/docker-compose/local-dev-services.yml"

docker-services-up:
	docker-compose -f ${COMPOSE_FILE_SERVICES} up -d

docker-services-down:
	docker-compose -f ${COMPOSE_FILE_SERVICES} down