from datetime import datetime

from pydantic import BaseModel, EmailStr
from typing import Optional


class CompanyCreate(BaseModel):
    name: str
    industry: Optional[str] = None
    email: Optional[EmailStr] = None


class CompanyUpdate(BaseModel):
    name: Optional[str] = None
    industry: Optional[str] = None
    email: Optional[EmailStr] = None


class CompanyRead(BaseModel):
    accountID: int
    name: str
    industry: Optional[str]
    email: Optional[EmailStr]
    created_date: datetime
    updated_date: datetime

    model_config = {"from_attributes": True}
