from pydantic import BaseModel
from typing import Optional


class CreateCrashInjuries(BaseModel):
    crash_record_id: str
    injuries_fatal: Optional[int]
    injuries_incapacitating: Optional[int]
    injuries_other: Optional[int]


class ReadCrashInjuries(CreateCrashInjuries):
    pass
