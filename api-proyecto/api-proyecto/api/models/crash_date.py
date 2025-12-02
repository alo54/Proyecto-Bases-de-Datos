from pydantic import BaseModel


class CreateCrashDate(BaseModel):
    crash_record_id: str
    crash_day_of_week: int
    crash_month: int


class ReadCrashDate(CreateCrashDate):
    pass
