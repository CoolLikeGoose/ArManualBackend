from typing import List

from sqlalchemy.orm import Session

from app.models.trackpoint import TrackPoint


def get_batch(db: Session, ids: List[int]):
    return db.query(TrackPoint).filter(TrackPoint.trackpointID.in_(ids)).all()
