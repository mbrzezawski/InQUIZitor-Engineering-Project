SHELL := /bin/bash

.PHONY: start start.backend start.frontend start.db stop logs migrate rebuild

start:
	docker compose up --build

start.backend:
	docker compose up api

start.frontend:
	docker compose up web

start.db:
	docker compose up db

stop:
	docker compose down

logs:
	docker compose logs -f --tail=200

migrate:
	docker compose run --rm api alembic upgrade head

rebuild:
	docker compose build --no-cache

