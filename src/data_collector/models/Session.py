from typing import List

from pydantic import BaseModel, Field

from .ObjectId import PyObjectId


class ClickEvent(BaseModel):
    url: str
    timestamp: int


class HighlightEvent(BaseModel):
    text: str
    timestamp: int


class Session(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    user_id: str
    url: str
    title: str
    startedAt: int
    endedAt: int
    duration: float
    highlights: List[HighlightEvent]
    clicks: List[ClickEvent]
    scrollDepth: int
