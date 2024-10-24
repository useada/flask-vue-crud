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
    last_updated_at: float = None

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
        
        # Se `created_at` for fornecido, converta para timestamp
        if "created_at" in data:
            created_at_str = data["created_at"]
            created_at_dt = datetime.strptime(created_at_str, "%Y-%m-%dT%H:%M:%SZ")
            created_ts = created_at_dt.timestamp()
        else:
            # Caso contrário, use o timestamp atual
            created_ts = time()

        # Convertendo `last_updated_at` se estiver presente (pode ser None no caso de POST)
        last_updated_at = None
        if "last_updated_at" in data and data["last_updated_at"]:
            last_updated_at_str = data["last_updated_at"]
            last_updated_at_dt = datetime.strptime(last_updated_at_str, "%Y-%m-%dT%H:%M:%SZ")
            last_updated_at = last_updated_at_dt.timestamp()

        return User(
            username=data["user"],
            password=data["password"],
            roles=roles,
            preferences=UserPreferences(timezone=data["user_timezone"]),
            active=data["is_user_active"],
            created_ts=created_ts,
            last_updated_at=last_updated_at
        )

    def to_json(self):
        """Converte uma instância de User para JSON no formato especificado"""
        created_at_dt = datetime.fromtimestamp(self.created_ts)
        created_at_str = created_at_dt.strftime("%Y-%m-%dT%H:%M:%SZ")

        last_updated_at_str = None
        if self.last_updated_at:
            last_updated_at_dt = datetime.fromtimestamp(self.last_updated_at)
            last_updated_at_str = last_updated_at_dt.strftime("%Y-%m-%dT%H:%M:%SZ")

        return {
            "user": self.username,
            "password": self.password,
            "is_user_admin": "admin" in self.roles,
            "is_user_manager": "manager" in self.roles,
            "is_user_tester": "tester" in self.roles,
            "user_timezone": self.preferences.timezone,
            "is_user_active": self.active,
            "created_at": created_at_str,
            "last_updated_at": last_updated_at_str
        }
