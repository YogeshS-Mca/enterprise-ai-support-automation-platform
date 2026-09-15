from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from backend.app.database.connection import Base
from backend.app.repositories.sqlalchemy_incident_repository import (
    SQLAlchemyIncidentRepository,
)
from backend.app.schemas.incident import (
    IncidentCreate,
    IncidentPriority,
    IncidentStatus,
)


TEST_DATABASE_URL = "sqlite:///:memory:"


engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def setup_function() -> None:
    """
    Create a fresh database schema before each test.
    """
    Base.metadata.create_all(bind=engine)


def teardown_function() -> None:
    """
    Remove the database schema after each test.
    """
    Base.metadata.drop_all(bind=engine)


def test_create_incident():
    with TestingSessionLocal() as db:
        repository = SQLAlchemyIncidentRepository(db)

        incident = IncidentCreate(
            title="Database connection failure",
            description="Production database is unavailable.",
            priority=IncidentPriority.CRITICAL,
        )

        created = repository.create(incident)

        assert created.incident_id is not None
        assert created.title == "Database connection failure"
        assert created.priority == IncidentPriority.CRITICAL
        assert created.status == IncidentStatus.NEW


def test_get_incident_by_id():
    with TestingSessionLocal() as db:
        repository = SQLAlchemyIncidentRepository(db)

        incident = IncidentCreate(
            title="VPN unavailable",
            description="Users cannot connect to the corporate VPN.",
            priority=IncidentPriority.HIGH,
        )

        created = repository.create(incident)

        result = repository.get_by_id(created.incident_id)

        assert result is not None
        assert result.incident_id == created.incident_id
        assert result.title == "VPN unavailable"


def test_get_missing_incident():
    from uuid import uuid4

    with TestingSessionLocal() as db:
        repository = SQLAlchemyIncidentRepository(db)

        result = repository.get_by_id(uuid4())

        assert result is None


def test_list_incidents():
    with TestingSessionLocal() as db:
        repository = SQLAlchemyIncidentRepository(db)

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
        assert incidents[0].title == "Email outage"
        assert incidents[1].title == "Laptop issue"