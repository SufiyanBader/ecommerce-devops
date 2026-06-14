from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
import os
import redis
import json

router = APIRouter(prefix="/notifications", tags=["notifications"])

REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379")
redis_client = redis.from_url(REDIS_URL)

class NotificationRequest(BaseModel):
    user_id: int
    type: str
    message: str
    metadata: Optional[dict] = None

class NotificationResponse(BaseModel):
    status: str
    message: str
    queued: bool

@router.post("/send", response_model=NotificationResponse)
def send_notification(notification: NotificationRequest):
    payload = notification.model_dump()
    redis_client.lpush("notifications", json.dumps(payload))
    return NotificationResponse(
        status="queued",
        message=f"Notification queued for user {notification.user_id}",
        queued=True
    )

@router.get("/queue/length")
def queue_length():
    length = redis_client.llen("notifications")
    return {"queue_length": length}

@router.get("/queue/peek")
def peek_queue():
    items = redis_client.lrange("notifications", 0, 4)
    return {"items": [json.loads(i) for i in items]}