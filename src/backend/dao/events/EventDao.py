from typing import Callable, List, Optional
from backend.models.stored.events.StoredEvent import StoredEvent
from sqlmodel import Session


class EventDao:
    def __init__(self, session: Session):
        self.session = session

    def create(self, event: StoredEvent) -> StoredEvent:
        self.session.add(event)
        self.session.commit()
        self.session.refresh(event)
        return event

    def get(self, event_id: int) -> Optional[StoredEvent]:
        return self.session.get(StoredEvent, event_id)
    
    def get_or_throw(self, event_id: int) -> StoredEvent:
        event_op = self.get(event_id)
        if not event_op:
            raise KeyError("Event with id: " + event_id + " not found.")

    def update(self, event_id: int, operator: Callable[[StoredEvent], None]) -> Optional[StoredEvent]:
        event = self.get_or_throw(event_id)
        operator(event)
        self.session.add(event)
        self.session.commit()
        self.session.refresh(event)
        return event