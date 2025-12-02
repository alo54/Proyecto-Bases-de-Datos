from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.entities.base import Base

class CrashClassification(Base):
    __tablename__ = "crash_classification"

    crash_record_id: Mapped[str] = mapped_column(
        String(128),
        ForeignKey("crashes.crash_record_id"),
        primary_key=True
    )
    first_crash_type: Mapped[str | None] = mapped_column(String(100))
    crash_type: Mapped[str | None] = mapped_column(String(100))
    prim_contributory_cause: Mapped[str | None] = mapped_column(String(255))
    sec_contributory_cause: Mapped[str | None] = mapped_column(String(255))
    damage: Mapped[str | None] = mapped_column(String(100))
    hit_and_run_i: Mapped[bool | None] = mapped_column(Boolean)

    crash = relationship("Crash", back_populates="classification")
