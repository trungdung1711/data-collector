from data_collector.models import Session
from data_collector.db import collection


class SessionRepo:
    @classmethod
    async def insert(cls, session: Session):
        session_dict = session.model_dump(by_alias=True)
        await collection.insert_one(session_dict)
        return session
