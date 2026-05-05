from typing import Optional

from sqlalchemy.orm import Session

from app.models.manual import Manual


def get_manual(db: Session, manual_id: int) -> Optional[Manual]:
    return db.query(Manual).filter(Manual.manualID == manual_id).first()
