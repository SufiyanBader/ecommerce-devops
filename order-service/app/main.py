from fastapi import FastAPI
from app.routers import orders
from app.database import Base, engine
from app.core.config import settings

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Order Service",
    version=settings.VERSION,
    description="Handles order placement and tracking"
)

@app.get("/health")
def health():
    return {"status": "healthy", "service": settings.SERVICE_NAME}

app.include_router(orders.router)