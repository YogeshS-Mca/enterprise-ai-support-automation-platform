from fastapi import FastAPI

app = FastAPI(
    title="Enterprise AI Support Platform",
    description="AI-powered IT support and autonomous incident resolution platform",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "ai-support-platform",
    }   