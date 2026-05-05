from typing import Optional
from pydantic import BaseModel


class Vector3Read(BaseModel):
    x: float
    y: float
    z: float


class ContentRead(BaseModel):
    header: Optional[str] = None
    text: Optional[str] = None