from dataclasses import dataclass
from typing import Optional


@dataclass
class Product:
    id: str
    image: str
    gender: str
    color: str
    description: str
    description_blip: str
    season: Optional[str]
