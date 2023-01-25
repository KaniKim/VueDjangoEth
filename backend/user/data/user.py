import datetime
from dataclasses import dataclass

@dataclass
class User:
    id: str
    name: str
    email: str
    password: str
    is_staff: bool
    is_active: bool
    is_superuser: bool
    login_at: datetime.datetime
    created_at: datetime.datetime
    updated_at: datetime.datetime
    ethereum_address: str