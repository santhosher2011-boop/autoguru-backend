from app.models.car import Car
async def compare_cars(left: Car, right: Car) -> str:
    prompt = f"Compare {left.make} {left.model} vs {right.make} {right.model} in 3 concise bullets."
    # TODO: call LLM
    return "AI summary will appear here."
