from fastapi import FastAPI
from app.routers import notifications
from app.core.config import settings

app = FastAPI(
    title="Notification Service",
    version=settings.VERSION,
    description="Handles notifications via Redis queue"
)

@app.get("/health")
def health():
    return {"status": "healthy", "service": settings.SERVICE_NAME}

app.include_router(notifications.router)