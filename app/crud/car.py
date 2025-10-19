from app.models.car import Car
from beanie.operators import In
async def list_cars(make=None, price_max=None, fuel=None, limit=20, skip=0):
    q = Car.find()
    if make:       q = q.find(Car.make == make)
    if price_max:  q = q.find(Car.variants.price_inr <= price_max)
    if fuel:       q = q.find(In(Car.variants.fuel, fuel))
    return await q.limit(limit).skip(skip).to_list()
async def get_car(car_id: str) -> Car | None:
    return await Car.get(car_id)
