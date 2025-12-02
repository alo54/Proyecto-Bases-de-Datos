from sqlalchemy import Boolean, String, BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.entities.base import Base

class VehicleViolations(Base):
    __tablename__ = "vehicle_violations"

    vehicle_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("vehicle.vehicle_id"),
        primary_key=True
    )
    cmrc_veh_i: Mapped[bool | None] = mapped_column(Boolean)
    exceed_speed_limit_i: Mapped[bool | None] = mapped_column(Boolean)
    hazmat_present_i: Mapped[bool | None] = mapped_column(Boolean)
    vehicle_defect: Mapped[str | None] = mapped_column(String(100))

    vehicle = relationship("Vehicle", back_populates="violations")
