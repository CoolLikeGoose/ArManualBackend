# FILE: app/schemas/interactionpoint.py
import json
from typing import Any, Dict, Optional

from pydantic import BaseModel, field_validator

from app.schemas.common import ContentRead, Vector3Read


class InteractionPointCreate(BaseModel):
    interactionPointID: int
    position: Optional[Dict[str, Any]] = None
    content: Optional[Dict[str, Any]] = None


class InteractionPointUpdate(BaseModel):
    position: Optional[Dict[str, Any]] = None
    content: Optional[Dict[str, Any]] = None


class InteractionPointRead(BaseModel):
    interactionPointID: int
    trackpointID: int
    position: Vector3Read
    content: ContentRead

    @field_validator("position", mode="before")
    def parse_position(cls, v):
        if isinstance(v, str):
            return json.loads(v)
        return v

    @field_validator("content", mode="before")
    def parse_content(cls, v):
        if isinstance(v, str):
            return json.loads(v)
        return v

    model_config = {"from_attributes": True}
