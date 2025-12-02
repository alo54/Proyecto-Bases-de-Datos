from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm.session import Session

from api.models.people import CreatePeople, ReadPeople
from db.session import DBSessionManager
from db.entities.people import People
from util.logger import LoggerSessionManager


class PeopleRouter:
    router = APIRouter(prefix="/people", tags=["People"])

    def __init__(self, db_session_manager: DBSessionManager, logger_session_manager: LoggerSessionManager):
        self.db_session_manager = db_session_manager
        self.logger_session = logger_session_manager
        self.logger = logger_session_manager.get_logger(__name__)

        self.router = APIRouter(prefix="/people", tags=["People"])

        self.router.add_api_route("/", self.list, methods=["GET"], response_model=list[ReadPeople])
        self.router.add_api_route("/{people_id}", self.get, methods=["GET"], response_model=ReadPeople)
        self.router.add_api_route("/", self.create, methods=["POST"], response_model=ReadPeople)
        self.router.add_api_route("/{people_id}", self.update, methods=["PUT"], response_model=ReadPeople)
        self.router.add_api_route("/{people_id}", self.delete, methods=["DELETE"])

    def list(self, request: Request):
        db_session: Session = request.state.db_session
        self.logger.info("Querying all people")
        return db_session.query(People).all()

    def get(self, people_id: str, request: Request):
        db_session: Session = request.state.db_session
        self.logger.info(f"Getting person with id: {people_id}")
        record = db_session.query(People).get(people_id)
        if not record:
            return JSONResponse(status_code=404, content={"error_description": "Not found"})
        return record

    def create(self, data: CreatePeople, request: Request):
        db_session: Session = request.state.db_session
        new_record = People(**data.model_dump())
        db_session.add(new_record)
        db_session.flush()
        return new_record

    def update(self, people_id: str, data: CreatePeople, request: Request):
        db_session: Session = request.state.db_session
        record = db_session.query(People).get(people_id)
        if not record:
            raise HTTPException(status_code=404, detail="Not found")

        for key, value in data.model_dump().items():
            setattr(record, key, value)

        db_session.flush()
        return record

    def delete(self, people_id: str, request: Request):
        db_session: Session = request.state.db_session
        record = db_session.query(People).get(people_id)
        if not record:
            raise HTTPException(status_code=404, detail="Not found")

        db_session.delete(record)
        return {"message": "People record deleted"}
