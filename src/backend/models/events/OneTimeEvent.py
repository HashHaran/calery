from typing import List

from pydantic import BaseModel

from src.backend.models.events import TimeFrame
from src.backend.models.users import User


class OneTimeEvent(BaseModel):
    time_frame: TimeFrame
    scheduled_by: User
    _participants: List[User]
    description: str

    @property
    def all_participants(self) -> List[User]:
        return self._participants + [self.scheduled_by]

    @property
    def participants_without_scheduler(self):
        return self._participants
