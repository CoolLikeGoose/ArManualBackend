from typing import List
from pydantic import BaseModel


class IdList(BaseModel):
    ids: List[int]
