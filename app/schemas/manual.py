# FILE: app/schemas/manual.py
from typing import Any, Dict, List, Optional

from pydantic import BaseModel

from app.schemas.scenary import ScenaryRead


class ManualCreate(BaseModel):
    companyID: int
    name: str
    status: Optional[str] = None
    trackPoints: Optional[int] = None
    meta: Optional[Dict[str, Any]] = None


class ManualUpdate(BaseModel):
    name: Optional[str] = None
    status: Optional[str] = None
    trackPoints: Optional[int] = None
    meta: Optional[Dict[str, Any]] = None


class ManualRead(BaseModel):
    manualID: int
    companyID: int
    name: str
    status: Optional[str] = None
    scenarios: List[ScenaryRead] = []
    trackPoints: Optional[int] = None
    meta: Optional[Dict[str, Any]] = None

    model_config = {"from_attributes": True}
