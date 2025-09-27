from data_collector.models import Session
from data_collector.schemas import session_schema
from data_collector.repository.session_repo import SessionRepo


async def create_session(
    session_create: session_schema.SessionCreate,
    user_id: str,
) -> session_schema.SessionResponse:
    session = Session(user_id=user_id, **session_create.model_dump())

    await SessionRepo.insert(session)
    return session_schema.SessionResponse(state=200)
