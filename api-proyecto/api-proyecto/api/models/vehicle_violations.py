from pydantic import BaseModel
from typing import Optional


class CreateVehicleViolation(BaseModel):
    vehicle_id: int
    cmrc_veh_i: Optional[bool]
    exceed_speed_limit_i: Optional[bool]
    hazmat_present_i: Optional[bool]
    vehicle_defect: Optional[str]


class ReadVehicleViolation(CreateVehicleViolation):
    pass
