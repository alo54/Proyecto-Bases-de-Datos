from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from api.models.vehicle_violations import CreateVehicleViolation, ReadVehicleViolation
from db.entities.vehicle_violations import VehicleViolations
from db.session import DBSessionManager
from util.logger import LoggerSessionManager


class VehicleViolationsRouter:
    router = APIRouter(prefix="/vehicle-violations", tags=["Vehicle Violations"])

    def __init__(self, db_session_manager: DBSessionManager, logger_session_manager: LoggerSessionManager):
        self.db_session_manager = db_session_manager
        self.logger = logger_session_manager.get_logger(__name__)

        self.router = APIRouter(
            prefix="/vehicle-violations",
            tags=["Vehicle Violations"]
        )

        self.router.add_api_route("/", self.list, methods=["GET"], response_model=list[ReadVehicleViolation])
        self.router.add_api_route("/{vehicle_id}", self.get, methods=["GET"], response_model=ReadVehicleViolation)
        self.router.add_api_route("/", self.create, methods=["POST"], response_model=ReadVehicleViolation)
        self.router.add_api_route("/{vehicle_id}", self.update, methods=["PUT"], response_model=ReadVehicleViolation)
        self.router.add_api_route("/{vehicle_id}", self.delete, methods=["DELETE"])
    
    def list(self, request: Request, skip: int = 0, limit: int = 100):
        db: Session = request.state.db_session
        self.logger.info(f"Listing vehicle violations: skip={skip}, limit={limit}")
        return db.query(VehicleViolations).offset(skip).limit(limit).all()

    def get(self, vehicle_id: int, request: Request):
        db: Session = request.state.db_session
        self.logger.info(f"Retrieving violations for vehicle_id: {vehicle_id}")
        violation = db.query(VehicleViolations).get(vehicle_id)

        if not violation:
            return JSONResponse(status_code=404, content={"error_description": "Not found"})
        return violation

    def create(self, data: CreateVehicleViolation, request: Request):
        db: Session = request.state.db_session
        new_violation = VehicleViolations(**data.model_dump())
        db.add(new_violation)
        db.flush()
        return new_violation

    def update(self, vehicle_id: int, data: CreateVehicleViolation, request: Request):
        db: Session = request.state.db_session
        violation = db.query(VehicleViolations).get(vehicle_id)

        if not violation:
            raise HTTPException(status_code=404, detail="Not found")

        for key, value in data.model_dump().items():
            setattr(violation, key, value)

        db.flush()
        return violation

    def delete(self, vehicle_id: int, request: Request):
        db: Session = request.state.db_session
        violation = db.query(VehicleViolations).get(vehicle_id)

        if not violation:
            raise HTTPException(status_code=404, detail="Not found")

        db.delete(violation)
        return {"message": "Vehicle violation deleted"}
