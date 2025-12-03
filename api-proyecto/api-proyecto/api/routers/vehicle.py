from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from api.models.vehicle import CreateVehicle, ReadVehicle
from db.entities.vehicle import Vehicle
from db.session import DBSessionManager
from util.logger import LoggerSessionManager


class VehicleRouter:
    router = APIRouter(prefix="/vehicles", tags=["Vehicles"])

    def __init__(self, db_session_manager: DBSessionManager, logger_session_manager: LoggerSessionManager):
        self.db_session_manager = db_session_manager
        self.logger = logger_session_manager.get_logger(__name__)

        self.router = APIRouter(
            prefix="/vehicles",
            tags=["Vehicles"]
        )

        self.router.add_api_route("/", self.list, methods=["GET"], response_model=list[ReadVehicle])
        self.router.add_api_route("/{vehicle_id}", self.get, methods=["GET"], response_model=ReadVehicle)
        self.router.add_api_route("/", self.create, methods=["POST"], response_model=ReadVehicle)
        self.router.add_api_route("/{vehicle_id}", self.update, methods=["PUT"], response_model=ReadVehicle)
        self.router.add_api_route("/{vehicle_id}", self.delete, methods=["DELETE"])
    
    def list(self, request: Request, skip: int = 0, limit: int = 100):
        db: Session = request.state.db_session
        self.logger.info(f"Listing vehicle: skip={skip}, limit={limit}")
        return db.query(Vehicle).offset(skip).limit(limit).all()

    def get(self, vehicle_id: int, request: Request):
        db: Session = request.state.db_session
        self.logger.info(f"Retrieving vehicle with id: {vehicle_id}")
        veh = db.query(Vehicle).get(vehicle_id)
        if not veh:
            return JSONResponse(status_code=404, content={"error_description": "Not found"})
        return veh

    def create(self, data: CreateVehicle, request: Request):
        db: Session = request.state.db_session
        new_vehicle = Vehicle(**data.model_dump())
        db.add(new_vehicle)
        db.flush()
        return new_vehicle

    def update(self, vehicle_id: int, data: CreateVehicle, request: Request):
        db: Session = request.state.db_session
        veh = db.query(Vehicle).get(vehicle_id)
        if not veh:
            raise HTTPException(status_code=404, detail="Not found")

        for key, value in data.model_dump().items():
            setattr(veh, key, value)

        db.flush()
        return veh

    def delete(self, vehicle_id: int, request: Request):
        db: Session = request.state.db_session
        veh = db.query(Vehicle).get(vehicle_id)
        if not veh:
            raise HTTPException(status_code=404, detail="Not found")
        db.delete(veh)
        return {"message": "Vehicle deleted"}
