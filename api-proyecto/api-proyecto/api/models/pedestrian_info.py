from pydantic import BaseModel
from typing import Optional


class CreatePedestrianInfo(BaseModel):
    person_id: str
    pedpedal_action: Optional[str]
    pedpedal_visibility: Optional[str]
    pedpedal_location: Optional[str]


class ReadPedestrianInfo(CreatePedestrianInfo):
    pass
