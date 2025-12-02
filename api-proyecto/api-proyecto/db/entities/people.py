from sqlalchemy import String, Integer, TIMESTAMP, BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.entities.base import Base


class People(Base):
    __tablename__ = "people"

    person_id: Mapped[str] = mapped_column(String(50), primary_key=True)
    person_type: Mapped[str | None] = mapped_column(String(50))

    crash_record_id: Mapped[str | None] = mapped_column(
        String(128),
        ForeignKey("crashes.crash_record_id")
    )
    vehicle_id: Mapped[int | None] = mapped_column(
        BigInteger,
        ForeignKey("vehicle.vehicle_id")
    )
    crash_date: Mapped[str | None] = mapped_column(TIMESTAMP)

    sex: Mapped[str | None] = mapped_column(String(10))
    age: Mapped[int | None] = mapped_column(Integer)
    safety_equipment: Mapped[str | None] = mapped_column(String(200))
    airbag_deployed: Mapped[str | None] = mapped_column(String(100))
    injury_classification: Mapped[str | None] = mapped_column(String(100))

    crash = relationship("Crash", back_populates="people")
    vehicle = relationship("Vehicle", back_populates="people")
    driver_info = relationship("DriverInfo", back_populates="person", uselist=False)
    #pedestrian_info = relationship("PedestrianInfo", back_populates="person", uselist=False)
