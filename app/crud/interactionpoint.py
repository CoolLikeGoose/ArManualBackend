from typing import List

from sqlalchemy.orm import Session

from app.models.interactionpoint import InteractionPoint


def get_batch(db: Session, ids: List[int]):
    return db.query(InteractionPoint).filter(InteractionPoint.interactionPointID.in_(ids)).all()
