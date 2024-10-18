from dataclasses import dataclass, field
from typing import List
from datetime import datetime
from time import time

@dataclass
class UserPreferences:
    timezone: str

@dataclass
class User:
    username: str
    password: str
    roles: List[str]
    preferences: UserPreferences
    active: bool = True
    created_ts: float = field(default_factory=time)

    @staticmethod
    def from_json(data: dict):
        """Cria uma instância de User a partir do JSON fornecido"""
        roles = []
        if data.get("is_user_admin", False):
            roles.append("admin")
        if data.get("is_user_manager", False):
            roles.append("manager")
        if data.get("is_user_tester", False):
            roles.append("tester")

        # Convertendo `created_at` de string ISO para timestamp
        created_at_str = data["created_at"]
        created_at_dt = datetime.strptime(created_at_str, "%Y-%m-%dT%H:%M:%SZ")
        created_ts = created_at_dt.timestamp()

        return User(
            username=data["user"],
            password=data["password"],
            roles=roles,
            preferences=UserPreferences(timezone=data["user_timezone"]),
            active=data["is_user_active"],
            created_ts=created_ts
        )

    def to_json(self):
        """Converte uma instância de User para JSON no formato especificado"""
        created_at_dt = datetime.fromtimestamp(self.created_ts)
        created_at_str = created_at_dt.strftime("%Y-%m-%dT%H:%M:%SZ")

        return {
            "user": self.username,
            "password": self.password,
            "is_user_admin": "admin" in self.roles,
            "is_user_manager": "manager" in self.roles,
            "is_user_tester": "tester" in self.roles,
            "user_timezone": self.preferences.timezone,
            "is_user_active": self.active,
            "created_at": created_at_str
        }
