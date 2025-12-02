from pydantic import BaseModel
from typing import Optional


class CreateDriverInfo(BaseModel):
    person_id: str
    driver_action: Optional[str]
    driver_vision: Optional[str]
    physical_condition: Optional[str]
    bac_result_value: Optional[float]
    cell_phone_use: Optional[bool]
    drivers_license_class: Optional[str]


class ReadDriverInfo(CreateDriverInfo):
    pass
