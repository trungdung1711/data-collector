from typing import List
from pydantic import BaseModel


class ClickEvent(BaseModel):
    url: str
    timestamp: int


class HighlightEvent(BaseModel):
    text: str
    timestamp: int


class SessionCreate(BaseModel):
    url: str
    title: str
    startedAt: int
    endedAt: int
    duration: int
    hightlights: List[HighlightEvent]
    clicks: List[ClickEvent]
    scrollDepth: int


class SessionResponse(BaseModel):
    state: int
