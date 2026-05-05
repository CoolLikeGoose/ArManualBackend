from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.trackpoint import get_batch
from app.db import get_db
from app.schemas import TrackPointRead
from app.schemas.idList import IdList

router = APIRouter(prefix="/trackpoints", tags=["trackpoints"])


@router.post("/batch")
def get_track_points_batch(body: IdList, db: Session = Depends(get_db)):
    points = get_batch(db, body.ids)
    return {"items": points}
