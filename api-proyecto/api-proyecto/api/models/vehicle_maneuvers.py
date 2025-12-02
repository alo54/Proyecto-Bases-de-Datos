from pydantic import BaseModel
from typing import Optional


class CreateVehicleManeuver(BaseModel):
    vehicle_id: int
    maneuver: Optional[str] = None


class ReadVehicleManeuver(CreateVehicleManeuver):
    pass
