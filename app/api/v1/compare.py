import asyncio
from fastapi import APIRouter
from pydantic import BaseModel
from app.crud import car as crud
from app.services.ai import compare_cars
router = APIRouter()
class CompareRequest(BaseModel):
    left_id: str
    right_id: str
@router.post("/")
async def compare(payload: CompareRequest):
    left, right = await asyncio.gather(
        crud.get_car(payload.left_id), crud.get_car(payload.right_id))
    ai_summary = await compare_cars(left, right)
    return {"left": left, "right": right, "ai_summary": ai_summary}
