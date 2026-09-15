from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.app.api.v1.incidents import router as incidents_router
from backend.app.database.connection import Base, engine
from backend.app.models.incident import Incident


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Initialize database tables when the application starts.
    """
    Base.metadata.create_all(bind=engine)

    yield


app = FastAPI(
    title="Enterprise AI Support Platform",
    description=(
        "AI-powered IT support and autonomous incident resolution platform. "
        "The platform manages incidents, provides operational intelligence, "
        "and prepares incidents for automated diagnosis and remediation."
    ),
    version="0.1.0",
    lifespan=lifespan,
)


app.include_router(incidents_router)


@app.get(
    "/health",
    tags=["System"],
    summary="Health check",
    description="Verify that the Enterprise AI Support Platform is running.",
)
def health_check() -> dict[str, str]:
    """
    Return platform health information.
    """
    return {
        "status": "healthy",
        "service": "ai-support-platform",
    }