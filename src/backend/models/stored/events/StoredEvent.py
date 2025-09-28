from datetime import datetime
from typing import List
from sqlmodel import JSON, Column, SQLModel, Field, Relationship, create_engine, Session, select

class StoredEvent(SQLModel, table = True):
    id: str = Field(default=None, primary_key=True)
    start_time: datetime
    end_time: datetime
    scheduled_by: str = Field(foreign_key="user.id")
    description: str
    participants: List[str] = Field(default_factory=list, sa_column=Column(JSON))
