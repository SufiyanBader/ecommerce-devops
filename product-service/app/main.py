from fastapi import FastAPI
from app.routers import products
from app.database import Base, engine
from app.core.config import settings

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Product Service",
    version=settings.VERSION,
    description="Handles product catalog"
)

@app.get("/health")
def health():
    return {"status": "healthy", "service": settings.SERVICE_NAME}

app.include_router(products.router)