from typing import Any, Dict, Optional

from pydantic import BaseModel


class TrackPointCreate(BaseModel):
    manualID: int
    arucoID: Optional[int] = None
    sizeCm: Optional[float] = None
    trackpointName: Optional[str] = None
    description: Optional[str] = None
    meta: Optional[Dict[str, Any]] = None


class TrackPointUpdate(BaseModel):
    arucoID: Optional[int] = None
    sizeCm: Optional[float] = None
    trackpointName: Optional[str] = None
    description: Optional[str] = None
    meta: Optional[Dict[str, Any]] = None


class TrackPointRead(BaseModel):
    trackpointID: int
    manualID: int
    arucoID: Optional[int]
    sizeCm: Optional[float]
    trackpointName: Optional[str]
    description: Optional[str]
    meta: Optional[Dict[str, Any]]

    model_config = {"from_attributes": True}
