from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.scenariointeraction import list_scenario_interactions_for_scenary
from app.db import get_db

router = APIRouter(prefix="/scenarios", tags=["scenarios"])


@router.get("/{scenario_id}/interactions")
def get_scenario_interactions(scenario_id: int, db: Session = Depends(get_db)):
    interactions = list_scenario_interactions_for_scenary(db, scenario_id)
    return {"items": interactions}
