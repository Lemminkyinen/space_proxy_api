import datetime as dt
from dataclasses import dataclass
from enum import Enum

from pydantic import BaseModel


class Response(BaseModel):
    b64_img: bytes
    url: str


class Rover(str, Enum):
    curiosity = "curiosity"
    opportunity = "opportunity"
    spirit = "spirit"
    perseverance = "perseverance"


@dataclass
class RoverInfo:
    name: str
    cameras: list[str]
    min_date: dt.date
    max_date: dt.date