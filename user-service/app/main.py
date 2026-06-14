from fastapi import FastAPI
from app.routers import auth, users
from app.database import Base, engine
from app.core.config import settings

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="User Service",
    version=settings.VERSION,
    description="Handles user registration and authentication"
)

# Health check — Prometheus and K8s will ping this
@app.get("/health")
def health():
    return {"status": "healthy", "service": settings.SERVICE_NAME}

# Metrics endpoint placeholder
@app.get("/metrics-info")
def metrics():
    return {"service": settings.SERVICE_NAME, "version": settings.VERSION}

# Routers
app.include_router(auth.router)
app.include_router(users.router)