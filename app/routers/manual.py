from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.manual import get_manual
from app.db import get_db
from app.schemas.manual import ManualRead

router = APIRouter(prefix="/manuals", tags=["manuals"])


@router.get("/{manual_id}", response_model=ManualRead)
def get_manual_endpoint(manual_id: int, db: Session = Depends(get_db)):
    manual = get_manual(db, manual_id)
    if not manual:
        raise HTTPException(status_code=404, detail="Manual not found")
    return ManualRead.model_validate(manual, from_attributes=True)
