from fastapi import APIRouter, Depends
from data_collector.auth import verify_token
from data_collector.types import Payload
from data_collector.services import session_service
from data_collector.schemas import session_schema


router = APIRouter(
    prefix="/api/v1/sessions",
    tags=["sessions"],
)


@router.post("/", response_model=session_schema.SessionResponse)
async def create_session(
    session_create: session_schema.SessionCreate,
    payload: Payload = Depends(verify_token),
):
    user_id = payload["sub"]
    return await session_service.create_session(session_create, user_id)
