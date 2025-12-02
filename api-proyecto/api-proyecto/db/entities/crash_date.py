from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.entities.base import Base

class CrashDate(Base):
    __tablename__ = "crash_date"

    crash_record_id: Mapped[str] = mapped_column(
        String(128),
        ForeignKey("crashes.crash_record_id"),
        primary_key=True
    )
    crash_day_of_week: Mapped[int | None] = mapped_column(Integer)
    crash_month: Mapped[int | None] = mapped_column(Integer)

    crash = relationship("Crash", back_populates="date_info")
