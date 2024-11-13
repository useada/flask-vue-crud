from dataclasses import dataclass, field
from typing import List
from datetime import datetime
from time import time


@dataclass
class Bar:
    timestamp: int
    open: float
    close: float
    high: float
    low: float
    volume: int
    turnover: float

    @staticmethod
    def from_json(data: dict):
        return Bar(
            timestamp=data["timestamp"],
            open=data["open"],
            close=data["close"],
            high=data["high"],
            low=data["low"],
            volume=data["volume"],
            turnover=data["turnover"],
        )

    def to_json(self):
        return {
            "timestamp": self.timestamp,
            "open": self.open,
            "close": self.close,
            "high": self.high,
            "low": self.low,
            "volume": self.volume,
            "turnover": self.turnover,
        }
