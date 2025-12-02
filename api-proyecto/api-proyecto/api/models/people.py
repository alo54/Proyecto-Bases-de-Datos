from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class CreatePeople(BaseModel):
    person_id: str
    person_type: Optional[str]
    crash_record_id: Optional[str]
    vehicle_id: Optional[int]
    crash_date: Optional[datetime]
    sex: Optional[str]
    age: Optional[int]
    safety_equipment: Optional[str]
    airbag_deployed: Optional[str]
    injury_classification: Optional[str]


class ReadPeople(CreatePeople):
    pass
