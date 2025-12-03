from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from api.models.vehicle_maneuvers import CreateVehicleManeuver, ReadVehicleManeuver
from db.entities.vehicle_maneuvers import VehicleManeuvers
from db.session import DBSessionManager
from util.logger import LoggerSessionManager


class VehicleManeuversRouter:
    router = APIRouter(prefix="/vehicle-maneuvers", tags=["Vehicle Maneuvers"])

    def __init__(self, db_session_manager: DBSessionManager, logger_session_manager: LoggerSessionManager):
        self.db_session_manager = db_session_manager
        self.logger = logger_session_manager.get_logger(__name__)

        self.router = APIRouter(
            prefix="/vehicle-maneuvers",
            tags=["Vehicle Maneuvers"]
        )

        self.router.add_api_route("/", self.list, methods=["GET"], response_model=list[ReadVehicleManeuver])
        self.router.add_api_route("/{vehicle_id}", self.get, methods=["GET"], response_model=ReadVehicleManeuver)
        self.router.add_api_route("/", self.create, methods=["POST"], response_model=ReadVehicleManeuver)
        self.router.add_api_route("/{vehicle_id}", self.update, methods=["PUT"], response_model=ReadVehicleManeuver)
        self.router.add_api_route("/{vehicle_id}", self.delete, methods=["DELETE"])

    def list(self, request: Request, skip: int = 0, limit: int = 100):
        db: Session = request.state.db_session
        self.logger.info(f"Listing vehicle_maneuvers: skip={skip}, limit={limit}")
        return db.query(VehicleManeuvers).offset(skip).limit(limit).all()

    def get(self, vehicle_id: int, request: Request):
        db: Session = request.state.db_session
        self.logger.info(f"Retrieving maneuver for vehicle_id: {vehicle_id}")
        maneuver = db.query(VehicleManeuvers).filter(VehicleManeuvers.vehicle_id == vehicle_id).first()
        if not maneuver:
            return JSONResponse(status_code=404, content={"error_description": "Not found"})
        return maneuver

    def create(self, data: CreateVehicleManeuver, request: Request):
        db: Session = request.state.db_session
        new_maneuver = VehicleManeuvers(**data.model_dump())
        db.add(new_maneuver)
        db.flush()
        return new_maneuver

    def update(self, vehicle_id: int, data: CreateVehicleManeuver, request: Request):
        db: Session = request.state.db_session
        maneuver = db.query(VehicleManeuvers).filter(VehicleManeuvers.vehicle_id == vehicle_id).first()

        if not maneuver:
            raise HTTPException(status_code=404, detail="Not found")

        for key, value in data.model_dump().items():
            setattr(maneuver, key, value)

        db.flush()
        return maneuver

    def delete(self, vehicle_id: int, request: Request):
        db: Session = request.state.db_session
        maneuver = db.query(VehicleManeuvers).filter(VehicleManeuvers.vehicle_id == vehicle_id).first()

        if not maneuver:
            raise HTTPException(status_code=404, detail="Not found")

        db.delete(maneuver)
        return {"message": "Vehicle maneuver deleted"}
