from fastapi import APIRouter, Query
from app.crud import car as crud
router = APIRouter()
@router.get("/")
async def cars(make: str | None = None, price_max: int | None = None,
               fuel: list[str] = Query(None), limit: int = 20, skip: int = 0):
    return await crud.list_cars(make, price_max, fuel, limit, skip)
@router.get("/{car_id}")
async def car_detail(car_id: str):
    return await crud.get_car(car_id)
