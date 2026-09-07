from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.app.models.incident import Incident
from backend.app.repositories.incident_repository import IncidentRepository
from backend.app.schemas.incident import (
    IncidentCreate,
    IncidentResponse,
    IncidentStatus,
)


class SQLAlchemyIncidentRepository(IncidentRepository):
    """
    SQLAlchemy implementation of the IncidentRepository contract.

    This repository is responsible for persisting and retrieving incidents
    using SQLAlchemy and the configured relational database.
    """

    def __init__(self, db: Session) -> None:
        self._db = db

    def create(self, incident: IncidentCreate) -> IncidentResponse:
        """
        Create and persist a new incident.
        """

        db_incident = Incident(
            title=incident.title,
            description=incident.description,
            priority=incident.priority.value,
            status=IncidentStatus.NEW.value,
        )

        self._db.add(db_incident)
        self._db.commit()
        self._db.refresh(db_incident)

        return IncidentResponse.model_validate(db_incident)

    def get_by_id(self, incident_id: UUID) -> IncidentResponse | None:
        """
        Retrieve an incident by its unique identifier.
        """

        statement = select(Incident).where(
            Incident.incident_id == str(incident_id)
        )

        db_incident = self._db.scalar(statement)

        if db_incident is None:
            return None

        return IncidentResponse.model_validate(db_incident)

    def list_all(self) -> list[IncidentResponse]:
        """
        Return all incidents ordered by creation time.
        """

        statement = select(Incident).order_by(Incident.created_at)

        db_incidents = self._db.scalars(statement).all()

        return [
            IncidentResponse.model_validate(incident)
            for incident in db_incidents
        ]