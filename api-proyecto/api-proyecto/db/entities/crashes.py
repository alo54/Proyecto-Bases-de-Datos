from sqlalchemy import String, Numeric, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.entities.base import Base

class Crash(Base):
    __tablename__ = "crashes"

    crash_record_id: Mapped[str] = mapped_column(String(128), primary_key=True)
    crash_date: Mapped[str | None] = mapped_column(TIMESTAMP, nullable=True)
    latitude: Mapped[float | None] = mapped_column(Numeric(9, 6))
    longitude: Mapped[float | None] = mapped_column(Numeric(9, 6))
    street_no: Mapped[str | None] = mapped_column(String(20))
    street_name: Mapped[str | None] = mapped_column(String(255))

    date_info = relationship("CrashDate", back_populates="crash", uselist=False)
    circumstances = relationship("CrashCircumstances", back_populates="crash", uselist=False)
    injuries = relationship("CrashInjuries", back_populates="crash", uselist=False)
    classification = relationship("CrashClassification", back_populates="crash", uselist=False)

    vehicles = relationship("Vehicle", back_populates="crash")
    people = relationship("People", back_populates="crash")
