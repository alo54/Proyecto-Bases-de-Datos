from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from api.models.crash_date import CreateCrashDate, ReadCrashDate
from db.entities.crash_date import CrashDate
from db.session import DBSessionManager
from util.logger import LoggerSessionManager


class CrashDateRouter:
    router = APIRouter(prefix="/crash_date", tags=["Crash Date"])

    def __init__(self, db_session_manager: DBSessionManager, logger_session_manager: LoggerSessionManager):
        self.db_session_manager = db_session_manager
        self.logger = logger_session_manager.get_logger(__name__)

        self.router = APIRouter(prefix="/crash_date", tags=["Crash Date"])

        self.router.add_api_route("/", self.list, methods=["GET"], response_model=list[ReadCrashDate])
        self.router.add_api_route("/{crash_record_id}", self.get, methods=["GET"], response_model=ReadCrashDate)
        self.router.add_api_route("/", self.create, methods=["POST"], response_model=ReadCrashDate)
        self.router.add_api_route("/{crash_record_id}", self.update, methods=["PUT"], response_model=ReadCrashDate)
        self.router.add_api_route("/{crash_record_id}", self.delete, methods=["DELETE"])

    def list(self, request: Request, skip: int = 0, limit: int = 100):
        db: Session = request.state.db_session
        self.logger.info(f"Listing crash_date: skip={skip}, limit={limit}")
        return db.query(CrashDate).offset(skip).limit(limit).all()

    def get(self, crash_record_id: str, request: Request):
        db: Session = request.state.db_session
        row = db.query(CrashDate).get(crash_record_id)
        if not row:
            return JSONResponse(status_code=404, content={"error_description": "Not found"})
        return row

    def create(self, data: CreateCrashDate, request: Request):
        db: Session = request.state.db_session
        new_row = CrashDate(**data.model_dump())
        db.add(new_row)
        db.flush()
        return new_row

    def update(self, crash_record_id: str, data: CreateCrashDate, request: Request):
        db: Session = request.state.db_session
        row = db.query(CrashDate).get(crash_record_id)
        if not row:
            raise HTTPException(status_code=404, detail="Not found")
        for key, value in data.model_dump().items():
            setattr(row, key, value)
        db.flush()
        return row

    def delete(self, crash_record_id: str, request: Request):
        db: Session = request.state.db_session
        row = db.query(CrashDate).get(crash_record_id)
        if not row:
            raise HTTPException(status_code=404, detail="Not found")
        db.delete(row)
        return {"message": "Crash date deleted"}
