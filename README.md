# AR Manuals API Backend

REST API backend for managing interactive manuals with augmented reality support. This backend is developed as part of a bachelor's thesis for the main [AR Manual project](https://github.com/CoolLikeGoose/ArManual).

This project in current state implements only the essential API endpoints required for the thesis project, with architecture designed to support future expansion and feature additions.

## Architecture and Structure

The backend is organized into several logical layers:

- **`models/`** — ORM models that define the structure of database entities
- **`crud/`** — CRUD operations for reading, creating, and updating data; abstracts direct ORM interactions
- **`schemas/`** — Pydantic schemas for API data validation and response format definition
- **`routers/`** — API endpoint implementations and client data access methods
- **`db.py`** — Database configuration and session management
- **`main.py`** — FastAPI application initialization and router registration

## Installation

### Requirements

- Python 3.8+
- pip

### Setup

1. Clone the repository and navigate to the directory:
```bash
cd ArManualBackend
```

2. Create a virtual environment:
```bash
python -m venv .venv
```

3. Activate the virtual environment:
   - **Windows (PowerShell)**:
   ```bash
   .venv\Scripts\Activate.ps1
   ```
   - **Linux/macOS**:
   ```bash
   source .venv/bin/activate
   ```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Server

Start the development server:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The server will be available at `http://localhost:8000`

### API Documentation

- **Swagger UI**: http://localhost:8000/docs

## Endpoints

### Manuals (`/manuals`)
- `GET /manuals/{manual_id}` — Get manual with scenarios

### Scenarios (`/scenarios`)
- `GET /scenarios/{scenario_id}/interactions` — Get scenario interactions

### Trackpoints (`/trackpoints`)
- `POST /trackpoints/batch` — Get trackpoints in batch

### Interaction Points (`/interactionpoints`)
- `POST /interactionpoints/batch` — Get interaction points in batch

## Database

The project uses SQLite for development. The database is automatically created on first run.

**Data file**: `data.sqlite`

## Technology Stack

- **FastAPI** — Async web framework
- **SQLAlchemy** — ORM
- **Pydantic** — Data validation
- **SQLite** — Relational database (development)
- **Uvicorn** — ASGI server