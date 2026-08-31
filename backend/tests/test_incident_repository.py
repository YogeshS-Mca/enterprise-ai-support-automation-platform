from backend.app.repositories.in_memory_incident_repository import (
    InMemoryIncidentRepository,
)
from backend.app.schemas.incident import (
    IncidentCreate,
    IncidentPriority,
    IncidentStatus,
)


def test_create_incident():
    repository = InMemoryIncidentRepository()

    incident = IncidentCreate(
        title="Database connection failure",
        description="Production database is unavailable.",
        priority=IncidentPriority.CRITICAL,
    )

    created = repository.create(incident)

    assert created.title == "Database connection failure"
    assert created.priority == IncidentPriority.CRITICAL
    assert created.status == IncidentStatus.NEW


def test_get_incident_by_id():
    repository = InMemoryIncidentRepository()

    incident = IncidentCreate(
        title="VPN unavailable",
        description="Users cannot connect to the corporate VPN.",
        priority=IncidentPriority.HIGH,
    )

    created = repository.create(incident)

    result = repository.get_by_id(created.incident_id)

    assert result is not None
    assert result.incident_id == created.incident_id


def test_list_incidents():
    repository = InMemoryIncidentRepository()

    first = IncidentCreate(
        title="Email outage",
        description="Corporate email service is unavailable.",
        priority=IncidentPriority.HIGH,
    )

    second = IncidentCreate(
        title="Laptop issue",
        description="User laptop cannot connect to the network.",
        priority=IncidentPriority.MEDIUM,
    )

    repository.create(first)
    repository.create(second)

    incidents = repository.list_all()

    assert len(incidents) == 2