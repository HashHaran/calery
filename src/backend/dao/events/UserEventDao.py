from typing import Callable, List, Optional
from backend.models.stored.events.StoredUserEvent import StoredUserEvent
from sqlmodel import Session


class UserEventDao:
    def __init__(self, session: Session):
        self.session = session

    def create(self, event: StoredUserEvent) -> StoredUserEvent:
        self.session.add(event)
        self.session.commit()
        self.session.refresh(event)
        return event

    def get(self, event_id: int) -> Optional[StoredUserEvent]:
        return self.session.get(StoredUserEvent, event_id)
    
    def get_or_throw(self, event_id: int) -> StoredUserEvent:
        event_op = self.get(event_id)
        if not event_op:
            raise KeyError("Event with id: " + event_id + " not found.")

    def update(self, event_id: int, operator: Callable[[StoredUserEvent], None]) -> Optional[StoredUserEvent]:
        event = self.get_or_throw(event_id)
        operator(event)
        self.session.add(event)
        self.session.commit()
        self.session.refresh(event)
        return event