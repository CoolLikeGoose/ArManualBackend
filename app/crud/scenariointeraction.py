from sqlalchemy.orm import Session

from app.models.scenariointeraction import ScenarioInteraction


def list_scenario_interactions_for_scenary(db: Session, scenary_id: int):
    return db.query(ScenarioInteraction).filter(
        ScenarioInteraction.scenarioID == scenary_id
    ).order_by(ScenarioInteraction.order).all()
