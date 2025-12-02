from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class CreateVehicle(BaseModel):
    vehicle_id: int
    crash_unit_id: int
    crash_record_id: str
    crash_date: datetime
    unit_no: Optional[int]
    unit_type: Optional[str]
    num_passengers: Optional[int]
    vehicle_year: Optional[int]
    make: Optional[str]
    model: Optional[str]


class ReadVehicle(CreateVehicle):
    pass
