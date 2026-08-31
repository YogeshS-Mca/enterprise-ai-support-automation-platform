from uuid import UUID

from backend.app.repositories.incident_repository import IncidentRepository
from backend.app.schemas.incident import (
    IncidentCreate,
    IncidentResponse,
)


class IncidentService:
    """
    Business logic layer for Incident Management.

    The service coordinates API requests with the persistence layer
    without exposing repository implementation details to the API layer.
    """

    def __init__(self, repository: IncidentRepository) -> None:
        self._repository = repository

    def create_incident(
        self,
        incident: IncidentCreate,
    ) -> IncidentResponse:
        """
        Create a new incident.
        """
        return self._repository.create(incident)

    def list_incidents(self) -> list[IncidentResponse]:
        """
        Return all incidents.
        """
        return self._repository.list_all()

    def get_incident(
        self,
        incident_id: UUID,
    ) -> IncidentResponse | None:
        """
        Retrieve an incident by its unique identifier.
        """
        return self._repository.get_by_id(incident_id)