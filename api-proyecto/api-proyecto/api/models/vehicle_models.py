from pydantic import BaseModel
from typing import Optional


class CreateVehicleModels(BaseModel):
    vehicle_id: int
    vehicle_use: Optional[str]
    vehicle_config: Optional[str]
    cargo_body_type: Optional[str]


class ReadVehicleModels(CreateVehicleModels):
    pass
