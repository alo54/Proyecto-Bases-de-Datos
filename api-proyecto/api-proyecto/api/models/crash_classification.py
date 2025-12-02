from pydantic import BaseModel
from typing import Optional


class CreateCrashClassification(BaseModel):
    crash_record_id: str
    first_crash_type: Optional[str]
    crash_type: Optional[str]
    prim_contributory_cause: Optional[str]
    sec_contributory_cause: Optional[str]
    damage: Optional[str]
    hit_and_run_i: Optional[bool]


class ReadCrashClassification(CreateCrashClassification):
    pass
