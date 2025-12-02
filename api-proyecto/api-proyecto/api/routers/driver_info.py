from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm.session import Session

from api.models.driver_info import CreateDriverInfo, ReadDriverInfo
from db.session import DBSessionManager
from db.entities.driver_info import DriverInfo
from util.logger import LoggerSessionManager


class DriverInfoRouter:
    router = APIRouter(prefix="/driver-info", tags=["Driver Info"])

    def __init__(self, db_session_manager: DBSessionManager, logger_session_manager: LoggerSessionManager):
        self.db_session_manager = db_session_manager
        self.logger_session = logger_session_manager
        self.logger = logger_session_manager.get_logger(__name__)

        self.router = APIRouter(prefix="/driver-info", tags=["Driver Info"])

        self.router.add_api_route("/", self.list, methods=["GET"], response_model=list[ReadDriverInfo])
        self.router.add_api_route("/{person_id}", self.get, methods=["GET"], response_model=ReadDriverInfo)
        self.router.add_api_route("/", self.create, methods=["POST"], response_model=ReadDriverInfo)
        self.router.add_api_route("/{person_id}", self.update, methods=["PUT"], response_model=ReadDriverInfo)
        self.router.add_api_route("/{person_id}", self.delete, methods=["DELETE"])

    def list(self, request: Request):
        db_session: Session = request.state.db_session
        self.logger.info("Listing all driver info records")
        return db_session.query(DriverInfo).all()

    def get(self, person_id: str, request: Request):
        db_session: Session = request.state.db_session
        self.logger.info(f"Getting driver info for person_id={person_id}")

        record = db_session.query(DriverInfo).get(person_id)
        if not record:
            return JSONResponse(status_code=404, content={"error_description": "Not found"})
        return record

    def create(self, data: CreateDriverInfo, request: Request):
        db_session: Session = request.state.db_session

        new_record = DriverInfo(**data.model_dump())
        db_session.add(new_record)
        db_session.flush()
        return new_record

    def update(self, person_id: str, data: CreateDriverInfo, request: Request):
        db_session: Session = request.state.db_session
        record = db_session.query(DriverInfo).get(person_id)

        if not record:
            raise HTTPException(status_code=404, detail="Not found")

        for key, value in data.model_dump().items():
            setattr(record, key, value)

        db_session.flush()
        return record

    def delete(self, person_id: str, request: Request):
        db_session: Session = request.state.db_session
        record = db_session.query(DriverInfo).get(person_id)

        if not record:
            raise HTTPException(status_code=404, detail="Not found")

        db_session.delete(record)
        return {"message": "Driver info deleted"}
