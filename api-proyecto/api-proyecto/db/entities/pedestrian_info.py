from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.entities.base import Base

class PedestrianInfo(Base):
    __tablename__ = "pedestrian_info"

    person_id: Mapped[str] = mapped_column(
        String(50),
        ForeignKey("people.person_id"),
        primary_key=True
    )

    pedpedal_action: Mapped[str | None] = mapped_column(String(100))
    pedpedal_visibility: Mapped[str | None] = mapped_column(String(100))
    pedpedal_location: Mapped[str | None] = mapped_column(String(100))

    person = relationship("People", back_populates="pedestrian_info")
