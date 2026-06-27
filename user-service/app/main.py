from fastapi import FastAPI, Request
from app.routers import auth, users
from app.database import Base, engine
from app.core.config import settings
import time
import os

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="User Service",
    version=settings.VERSION,
    description="Handles user registration and authentication"
)

# Request tracking for metrics
request_count = {}
request_duration = {}

@app.middleware("http")
async def track_metrics(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time

    path = request.url.path
    method = request.method
    status = response.status_code

    key = f"{method}_{path}_{status}"
    request_count[key] = request_count.get(key, 0) + 1
    if key not in request_duration:
        request_duration[key] = []
    request_duration[key].append(duration)

    return response

@app.get("/health")
def health():
    return {"status": "healthy", "service": settings.SERVICE_NAME}

@app.get("/metrics")
def metrics():
    lines = []
    for key, count in request_count.items():
        method, path, status = key.split("_", 2)
        lines.append(
            f'http_requests_total{{method="{method}",path="{path}",status="{status}"}} {count}'
        )
    for key, durations in request_duration.items():
        method, path, status = key.split("_", 2)
        avg = sum(durations) / len(durations)
        lines.append(
            f'http_request_duration_seconds_avg{{method="{method}",path="{path}"}} {avg:.4f}'
        )
    return "\n".join(lines)

app.include_router(auth.router)
app.include_router(users.router)