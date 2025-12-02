from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class CreateCrash(BaseModel):
    crash_record_id: str
    incident_date: Optional[datetime]
    latitude: Optional[float]
    longitude: Optional[float]
    street_no: Optional[str]
    street_name: Optional[str]


class ReadCrash(CreateCrash):
    pass
