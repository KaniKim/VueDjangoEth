import datetime
from dataclasses import dataclass

@dataclass
class User:
    id: str
    name: str
    email: str
    password: str
    is_active: bool
    is_superuser: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime