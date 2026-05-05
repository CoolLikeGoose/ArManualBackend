from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.interactionpoint import get_batch
from app.db import get_db
from app.schemas.interactionpoint import InteractionPointRead
from app.schemas.idList import IdList

router = APIRouter(prefix="/interactionpoints", tags=["interactionpoints"])


@router.post("/batch")
def get_interaction_points_batch(body: IdList, db: Session = Depends(get_db)):
    points = get_batch(db, body.ids)
    return {
        "items": [
            InteractionPointRead.model_validate(p, from_attributes=True)
            for p in points
        ]
    }
