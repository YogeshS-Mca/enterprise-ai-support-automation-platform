from abc import ABC, abstractmethod
from uuid import UUID

from backend.app.schemas.incident import (
    IncidentCreate,
    IncidentResponse,
)


class IncidentRepository(ABC):
    """Contract for incident persistence."""

    @abstractmethod
    def create(self, incident: IncidentCreate) -> IncidentResponse:
        """Create and persist an incident."""
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, incident_id: UUID) -> IncidentResponse | None:
        """Retrieve an incident by ID."""
        raise NotImplementedError

    @abstractmethod
    def list_all(self) -> list[IncidentResponse]:
        """Return all incidents."""
        raise NotImplementedError