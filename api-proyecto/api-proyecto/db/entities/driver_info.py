from sqlalchemy import Float, String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.entities.base import Base

class DriverInfo(Base):
    __tablename__ = "driver_info"

    person_id: Mapped[str] = mapped_column(
        String(50),
        ForeignKey("people.person_id"),
        primary_key=True
    )

    driver_action: Mapped[str | None] = mapped_column(String(50))
    driver_vision: Mapped[str | None] = mapped_column(String(50))
    physical_condition: Mapped[str | None] = mapped_column(String(50))
    bac_result_value: Mapped[float | None] = mapped_column(Float)
    cell_phone_use: Mapped[bool | None] = mapped_column(Boolean)
    drivers_license_class: Mapped[str | None] = mapped_column(String(10))

    person = relationship("People", back_populates="driver_info")
