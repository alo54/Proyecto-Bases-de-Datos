from pydantic import BaseModel


class CreateVehicleManeuver(BaseModel):
    vehicle_id: int
    maneuver: str


class ReadVehicleManeuver(CreateVehicleManeuver):
    pass
