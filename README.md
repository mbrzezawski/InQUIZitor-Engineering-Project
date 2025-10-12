# Development

## Local development (Docker Compose)

Prerequisites: Docker Desktop 4.x

### First run
1. Start all services:
   - `make start` (or `docker compose up --build`)
2. Open services:
   - API: http://localhost:8000/docs
   - Web: http://localhost:5173

### Useful commands
- Start only backend: `make start.backend`
- Start only frontend: `make start.frontend`
- Start only db: `make start.db`
- Stop all: `make stop`
- Logs (follow): `make logs`
- Run migrations: `make migrate`

### Notes
- Backend hot‑reload: mounted `./backend:/app`
- Frontend hot‑reload: mounted `./frontend:/usr/src/app`
- Postgres data persists in volume `pgdata`

### Troubleshooting
- If dependency changes are not picked up, rebuild images:
  - `make rebuild`
- If Vite dev server can’t resolve deps after first run:
  - remove `node_modules` volume: `docker volume rm inquizitor_node_modules`
- On macOS, if file change latency is high, consider disabling file indexing (Spotlight) on the repo directory.
