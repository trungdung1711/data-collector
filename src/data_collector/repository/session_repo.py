from data_collector.db import collection
from data_collector.models import Session


class SessionRepo:
    @classmethod
    async def insert(cls, session: Session):
        session_dict = session.model_dump(by_alias=True)
        await collection.insert_one(session_dict)
        return session
