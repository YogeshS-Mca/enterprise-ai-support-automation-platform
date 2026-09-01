from fastapi import FastAPI

from backend.app.api.v1.incidents import router as incidents_router


app = FastAPI(
    title="Enterprise AI Support Platform",
    description=(
        "AI-powered IT support and autonomous incident resolution platform. "
        "The platform manages incidents, provides operational intelligence, "
        "and prepares incidents for automated diagnosis and remediation."
    ),
    version="0.1.0",
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