from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from backend.app.repositories.in_memory_incident_repository import (
    InMemoryIncidentRepository,
)
from backend.app.schemas.incident import (
    IncidentCreate,
    IncidentResponse,
)
from backend.app.services.incident_service import IncidentService


router = APIRouter(
    prefix="/api/v1/incidents",
    tags=["Incidents"],
)


repository = InMemoryIncidentRepository()


def get_incident_service() -> IncidentService:
    """
    Dependency provider for the IncidentService.
    """
    return IncidentService(repository)


@router.post(
    "",
    response_model=IncidentResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create an incident",
    description=(
        "Create a new IT incident and assign it a unique identifier, "
        "priority, lifecycle status, and timestamps."
    ),
)
def create_incident(
    incident: IncidentCreate,
    service: IncidentService = Depends(get_incident_service),
) -> IncidentResponse:
    """
    Create a new incident.
    """
    return service.create_incident(incident)


@router.get(
    "",
    response_model=list[IncidentResponse],
    status_code=status.HTTP_200_OK,
    summary="List incidents",
    description="Return all incidents currently managed by the platform.",
)
def list_incidents(
    service: IncidentService = Depends(get_incident_service),
) -> list[IncidentResponse]:
    """
    List all incidents.
    """
    return service.list_incidents()


@router.get(
    "/{incident_id}",
    response_model=IncidentResponse,
    status_code=status.HTTP_200_OK,
    summary="Retrieve an incident",
    description="Retrieve a single incident using its unique identifier.",
)
def get_incident(
    incident_id: UUID,
    service: IncidentService = Depends(get_incident_service),
) -> IncidentResponse:
    """
    Retrieve an incident by ID.
    """

    incident = service.get_incident(incident_id)

    if incident is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Incident '{incident_id}' was not found.",
        )

    return incident