from datetime import datetime, timezone
from uuid import UUID, uuid4

from backend.app.repositories.incident_repository import IncidentRepository
from backend.app.schemas.incident import (
    IncidentCreate,
    IncidentResponse,
    IncidentStatus,
)


class InMemoryIncidentRepository(IncidentRepository):
    """In-memory implementation of the incident repository."""

    def __init__(self) -> None:
        self._incidents: dict[UUID, IncidentResponse] = {}

    def create(self, incident: IncidentCreate) -> IncidentResponse:
        now = datetime.now(timezone.utc)
        incident_id = uuid4()

        stored_incident = IncidentResponse(
            incident_id=incident_id,
            title=incident.title,
            description=incident.description,
            priority=incident.priority,
            status=IncidentStatus.NEW,
            created_at=now,
            updated_at=now,
        )

        self._incidents[incident_id] = stored_incident

        return stored_incident

    def get_by_id(self, incident_id: UUID) -> IncidentResponse | None:
        return self._incidents.get(incident_id)

    def list_all(self) -> list[IncidentResponse]:
        return list(self._incidents.values())