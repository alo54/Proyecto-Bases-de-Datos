from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy import select

from api.models.crashes import CreateCrash, ReadCrash
from db.entities.crashes import Crash
from db.session import DBSessionManager
from util.logger import LoggerSessionManager


class CrashesRouter:
    router = APIRouter(prefix="/crashes", tags=["Crashes"])

    def __init__(self, db_session_manager: DBSessionManager, logger_session_manager: LoggerSessionManager):
        self.db_session_manager = db_session_manager
        self.logger = logger_session_manager.get_logger(__name__)

        self.router = APIRouter(prefix="/crashes", tags=["Crashes"])

        self.router.add_api_route("/", self.list, methods=["GET"], response_model=list[ReadCrash])
        self.router.add_api_route("/{crash_record_id}", self.get, methods=["GET"], response_model=ReadCrash)
        self.router.add_api_route("/", self.create, methods=["POST"], response_model=ReadCrash)
        self.router.add_api_route("/{crash_record_id}", self.update, methods=["PUT"], response_model=ReadCrash)
        self.router.add_api_route("/{crash_record_id}", self.delete, methods=["DELETE"])

    def list(self, request: Request):
        db: Session = request.state.db_session
        self.logger.info("Fetching all crashes")
        return db.query(Crash).all()

    def get(self, crash_record_id: str, request: Request):
        db: Session = request.state.db_session
        self.logger.info(f"Fetching crash with ID: {crash_record_id}")
        crash = db.query(Crash).get(crash_record_id)
        if not crash:
            return JSONResponse(status_code=404, content={"error_description": "Not found"})
        return crash

    def create(self, data: CreateCrash, request: Request):
        db: Session = request.state.db_session
        new = Crash(**data.model_dump())
        db.add(new)
        db.flush()
        return new

    def update(self, crash_record_id: str, data: CreateCrash, request: Request):
        db: Session = request.state.db_session
        item = db.query(Crash).get(crash_record_id)
        if not item:
            raise HTTPException(404, "Not found")
        for k, v in data.model_dump().items():
            setattr(item, k, v)
        db.flush()
        return item

    def delete(self, crash_record_id: str, request: Request):
        db: Session = request.state.db_session
        item = db.query(Crash).get(crash_record_id)
        if not item:
            raise HTTPException(404, "Not found")
        db.delete(item)
        return {"message": "Crash deleted"}
