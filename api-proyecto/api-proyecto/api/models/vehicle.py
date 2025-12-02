from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class CreateVehicle(BaseModel):
    vehicle_id: int
    crash_unit_id: int
    crash_record_id: str
    crash_date: datetime
    unit_no: Optional[int] = None
    unit_type: Optional[str] = None
    num_passengers: Optional[int] = None
    vehicle_year: Optional[int] = None
    make: Optional[str] = None
    model: Optional[str] = None
    vehicle_type: Optional[str] = None


class ReadVehicle(CreateVehicle):
    pass
