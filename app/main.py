from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core import db
from app.api.v1 import cars, compare, emi, chat, search
app = FastAPI(title="AutoGuru Backend", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.on_event("startup")
async def startup(): await db.connect()
@app.on_event("shutdown")
async def shutdown(): await db.close()
app.include_router(cars.router, prefix="/api/v1/cars", tags=["cars"])
app.include_router(compare.router, prefix="/api/v1/compare", tags=["compare"])
app.include_router(emi.router, prefix="/api/v1/emi", tags=["emi"])
app.include_router(chat.router, prefix="/api/v1/chat", tags=["ai"])
app.include_router(search.router, prefix="/api/v1/search", tags=["search"])
