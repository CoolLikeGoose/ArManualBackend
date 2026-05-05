from typing import Any, Dict, Optional

from pydantic import BaseModel


class ScenarioInteractionCreate(BaseModel):
    scenarioID: int
    interactionPointID: int
    overrideContent: Optional[Dict[str, Any]] = None
    order: Optional[int] = None


class ScenarioInteractionUpdate(BaseModel):
    overrideContent: Optional[Dict[str, Any]] = None
    order: Optional[int] = None


class ScenarioInteractionRead(BaseModel):
    scenarioID: int
    interactionPointID: int
    overrideContent: Optional[Dict[str, Any]]
    order: Optional[int]

    model_config = {"from_attributes": True}
