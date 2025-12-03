from fastapi import APIRouter, HTTPException, Request
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from api.models.vehicle_models import CreateVehicleModels, ReadVehicleModels
from db.entities.vehicle_models import VehicleModels
from db.session import DBSessionManager
from util.logger import LoggerSessionManager


class VehicleModelsRouter:
    router = APIRouter(prefix="/vehicle-models", tags=["Vehicle Models"])

    def __init__(self, db_session_manager: DBSessionManager, logger_session_manager: LoggerSessionManager):
        self.db_session_manager = db_session_manager
        self.logger = logger_session_manager.get_logger(__name__)

        self.router = APIRouter(
            prefix="/vehicle-models",
            tags=["Vehicle Specs"]
        )

        self.router.add_api_route("/", self.list, methods=["GET"], response_model=list[ReadVehicleModels])
        self.router.add_api_route("/{vehicle_id}", self.get, methods=["GET"], response_model=ReadVehicleModels)
        self.router.add_api_route("/", self.create, methods=["POST"], response_model=ReadVehicleModels)
        self.router.add_api_route("/{vehicle_id}", self.update, methods=["PUT"], response_model=ReadVehicleModels)
        self.router.add_api_route("/{vehicle_id}", self.delete, methods=["DELETE"])
    
    def list(self, request: Request, skip: int = 0, limit: int = 100):
        db: Session = request.state.db_session
        self.logger.info(f"Listing vehicle_models: skip={skip}, limit={limit}")
        return db.query(VehicleModels).offset(skip).limit(limit).all()

    def get(self, vehicle_id: int, request: Request):
        db: Session = request.state.db_session
        self.logger.info(f"Retrieving vehicle model for vehicle_id: {vehicle_id}")
        model = db.query(VehicleModels).filter(VehicleModels.vehicle_id == vehicle_id).first()
        if not model:
            return JSONResponse(status_code=404, content={"error_description": "Not found"})
        return model

    def create(self, data: CreateVehicleModels, request: Request):
        db: Session = request.state.db_session
        new_model = VehicleModels(**data.model_dump())
        db.add(new_model)
        db.flush()
        return new_model

    def update(self, vehicle_id: int, data: CreateVehicleModels, request: Request):
        db: Session = request.state.db_session
        model = db.query(VehicleModels).filter(VehicleModels.vehicle_id == vehicle_id).first()
        if not model:
            raise HTTPException(status_code=404, detail="Not found")

        for key, value in data.model_dump().items():
            setattr(model, key, value)

        db.flush()
        return model

    def delete(self, vehicle_id: int, request: Request):
        db: Session = request.state.db_session
        model = db.query(VehicleModels).filter(VehicleModels.vehicle_id == vehicle_id).first()
        if not model:
            raise HTTPException(status_code=404, detail="Not found")

        db.delete(model)
        return {"message": "Vehicle model deleted"}
