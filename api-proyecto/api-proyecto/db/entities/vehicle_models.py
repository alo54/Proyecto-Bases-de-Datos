from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.entities.base import Base

class VehicleModels(Base):
    __tablename__ = "vehicle_specs"

    vehicle_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("vehicle.vehicle_id"),
        primary_key=True
    )

    vehicle_use: Mapped[str | None] = mapped_column(String(150))
    vehicle_config: Mapped[str | None] = mapped_column(String(150))
    cargo_body_type: Mapped[str | None] = mapped_column(String(150))

    vehicle = relationship("Vehicle", back_populates="models")
