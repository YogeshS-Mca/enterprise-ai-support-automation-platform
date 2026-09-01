from datetime import datetime
from enum import Enum
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


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
    """
    Request schema used when creating a new incident.
    """

    title: str = Field(
        min_length=5,
        max_length=200,
        description="Short, human-readable summary of the incident.",
        examples=["Production API returning HTTP 500 errors"],
    )

    description: str = Field(
        min_length=10,
        max_length=5000,
        description="Detailed description of the technical problem.",
        examples=[
            "The production customer API is returning HTTP 500 responses "
            "for approximately 30% of requests."
        ],
    )

    priority: IncidentPriority = Field(
        default=IncidentPriority.MEDIUM,
        description="Business impact and urgency of the incident.",
        examples=["high"],
    )


class IncidentResponse(BaseModel):
    """
    Response schema returned by the Incident Management API.
    """

    model_config = ConfigDict(
        from_attributes=True,
    )

    incident_id: UUID = Field(
        description="Unique identifier assigned to the incident."
    )

    title: str = Field(
        description="Short description of the incident."
    )

    description: str = Field(
        description="Detailed description of the incident."
    )

    priority: IncidentPriority = Field(
        description="Incident priority."
    )

    status: IncidentStatus = Field(
        description="Current lifecycle state of the incident."
    )

    created_at: datetime = Field(
        description="UTC timestamp when the incident was created."
    )

    updated_at: datetime = Field(
        description="UTC timestamp when the incident was last updated."
    )