from datetime import datetime
from enum import Enum
from uuid import UUID

from pydantic import BaseModel, Field


class IncidentPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class IncidentStatus(str, Enum):
    NEW = "new"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"


class IncidentCreate(BaseModel):
    title: str = Field(
        min_length=5,
        max_length=200,
        description="Short description of the incident",
    )

    description: str = Field(
        min_length=10,
        max_length=5000,
        description="Detailed description of the incident",
    )

    priority: IncidentPriority = Field(
        default=IncidentPriority.MEDIUM,
        description="Incident priority",
    )


class IncidentResponse(BaseModel):
    incident_id: UUID
    title: str
    description: str
    priority: IncidentPriority
    status: IncidentStatus
    created_at: datetime
    updated_at: datetime