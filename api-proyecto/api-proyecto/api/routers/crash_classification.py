from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm.session import Session

from api.models.crash_classification import CreateCrashClassification, ReadCrashClassification
from db.session import DBSessionManager
from db.entities.crash_classification import CrashClassification
from util.logger import LoggerSessionManager


class CrashClassificationRouter:
    router = APIRouter(prefix="/crash-classification", tags=["Crash Classification"])

    def __init__(self, db_session_manager: DBSessionManager, logger_session_manager: LoggerSessionManager):
        self.db_session_manager = db_session_manager
        self.logger_session = logger_session_manager
        self.logger = logger_session_manager.get_logger(__name__)

        self.router = APIRouter(prefix="/crash-classification", tags=["Crash Classification"])

        self.router.add_api_route("/", self.list, methods=["GET"], response_model=list[ReadCrashClassification])
        self.router.add_api_route("/{crash_record_id}", self.get, methods=["GET"], response_model=ReadCrashClassification)
        self.router.add_api_route("/", self.create, methods=["POST"], response_model=ReadCrashClassification)
        self.router.add_api_route("/{crash_record_id}", self.update, methods=["PUT"], response_model=ReadCrashClassification)
        self.router.add_api_route("/{crash_record_id}", self.delete, methods=["DELETE"])
    
    def list(self, request: Request, skip: int = 0, limit: int = 100):
        db: Session = request.state.db_session
        self.logger.info(f"Listing crash_classification: skip={skip}, limit={limit}")
        return db.query(CrashClassification).offset(skip).limit(limit).all()

    def get(self, crash_record_id: str, request: Request):
        db_session: Session = request.state.db_session
        self.logger.info(f"Getting crash classification for crash_record_id={crash_record_id}")

        record = db_session.query(CrashClassification).get(crash_record_id)
        if not record:
            return JSONResponse(status_code=404, content={"error_description": "Not found"})
        return record

    def create(self, data: CreateCrashClassification, request: Request):
        db_session: Session = request.state.db_session

        new_record = CrashClassification(**data.model_dump())
        db_session.add(new_record)
        db_session.flush()
        return new_record

    def update(self, crash_record_id: str, data: CreateCrashClassification, request: Request):
        db_session: Session = request.state.db_session
        record = db_session.query(CrashClassification).get(crash_record_id)

        if not record:
            raise HTTPException(status_code=404, detail="Not found")

        for key, value in data.model_dump().items():
            setattr(record, key, value)

        db_session.flush()
        return record

    def delete(self, crash_record_id: str, request: Request):
        db_session: Session = request.state.db_session
        record = db_session.query(CrashClassification).get(crash_record_id)

        if not record:
            raise HTTPException(status_code=404, detail="Not found")

        db_session.delete(record)
        return {"message": "Crash classification deleted"}
