from pydantic import BaseModel
from typing import Optional


class CreateCrashCircumstances(BaseModel):
    crash_record_id: str
    traffic_control_device: Optional[str]
    device_condition: Optional[str]
    weather_condition: Optional[str]
    lighting_condition: Optional[str]
    lane_cnt: Optional[int]
    roadway_surface_cond: Optional[str]
    road_defect: Optional[str]
    num_units: Optional[int]
    posted_speed_limit: Optional[int]
    intersection_related_i: Optional[bool]
    not_right_of_way_i: Optional[bool]


class ReadCrashCircumstances(CreateCrashCircumstances):
    pass
