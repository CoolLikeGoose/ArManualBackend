from typing import Any, Dict, Optional

from pydantic import BaseModel


class ScenaryCreate(BaseModel):
    manualID: int
    name: str
    type: Optional[str] = None
    category: Optional[str] = None
    note: Optional[str] = None
    content: Optional[Dict[str, Any]] = None
    order: Optional[int] = None


class ScenaryUpdate(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    category: Optional[str] = None
    note: Optional[str] = None
    content: Optional[Dict[str, Any]] = None
    order: Optional[int] = None


class ScenaryRead(BaseModel):
    scenarioID: int
    manualID: int
    name: str
    type: int
    category: Optional[str]
    note: Optional[str]
    order: Optional[int]

    model_config = {"from_attributes": True}
