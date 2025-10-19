from beanie import Document
from pydantic import BaseModel
from typing import List
class Variant(BaseModel):
    name: str
    price_inr: int
    fuel: str
    transmission: str
    mileage: float
class Car(Document):
    make: str
    model: str
    year: int
    body_type: str
    thumbnail: str
    images: List[str] = []
    variants: List[Variant]
    highlights: List[str]
    ai_summary: str
    class Settings:
        indexes = [
            "make",
            "model",
            [("make", 1), ("model", 1)],
            "variants.price_inr",
        ]
