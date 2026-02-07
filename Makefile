PROJECT_NAME = algo-bots
DCF = docker/docker-compose.dev.yml
DC = docker compose -p ${PROJECT_NAME} -f ${DCF}

BOT_IMPULSE_DAY = impulse_day_bot

# Базовые команды
build:
	${DC} build

up:
	${DC} up -d

down:
	${DC} down

restart:
	${DC} down
	${DC} build
	${DC} up -d

logs:
	${DC} logs ${BOT_IMPULSE_DAY}