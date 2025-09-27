from fastapi import APIRouter, Depends

from data_collector.auth import verify_token
from data_collector.types import Payload

router = APIRouter(prefix="/api/v1/me", tags=["me"])


@router.get("/")
def get_me(payload: Payload = Depends(verify_token)):
    return payload
