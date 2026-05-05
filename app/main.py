# FILE: app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db import engine, Base
from app.routers import (
    company,
    interactionpoint,
    manual,
    scenary,
    scenariointeraction,
    trackpoint,
)

app = FastAPI(title="Manuals API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(company.router)
app.include_router(manual.router)
app.include_router(scenary.router)
app.include_router(trackpoint.router)
app.include_router(interactionpoint.router)
app.include_router(scenariointeraction.router)


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
