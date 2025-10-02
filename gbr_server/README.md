GBR Server (FastAPI + Postgres)

Quick start (Docker)

```bash
# From workspace root
cd gbr_server
copy .env.example .env  # On Windows PowerShell: copy .env.example .env
# Then adjust .env values if needed

# Build and run
docker compose up -d --build

# Apply migrations
docker compose exec api alembic upgrade head
```

Local dev (without Docker)
```bash
cd gbr_server
python -m venv .venv
. .venv/Scripts/Activate.ps1
pip install -e .[dev]
copy .env.example .env
# Ensure Postgres is available and env vars set in .env
alembic upgrade head
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Endpoints
- GET `/health` – health check
- POST `/users` – create user
- POST `/users/login` – login
- GET `/users/me` – current user (JWT auth)

Migrations
- Create: `alembic revision -m "message" --autogenerate`
- Apply: `alembic upgrade head`

