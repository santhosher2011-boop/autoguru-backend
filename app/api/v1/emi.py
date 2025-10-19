from fastapi import APIRouter
router = APIRouter()
@router.get("/")
async def emi(price: int, down: int = 0, tenure: int = 60, roi: float = 9.5):
    principal = price - down
    r = roi / 12 / 100
    emi = principal * r * (1 + r) ** tenure / ((1 + r) ** tenure - 1)
    return {"emi": round(emi), "total": round(emi * tenure)}
