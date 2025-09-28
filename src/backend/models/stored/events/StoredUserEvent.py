from datetime import datetime
from sqlmodel import JSON, Column, SQLModel, Field, Relationship, create_engine, Session, select

class StoredUserEvent(SQLModel, table = True):
    user_id: str
    event_id: str
    start_time: datetime
    