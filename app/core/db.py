from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.models.car import Car
from app.core.config import settings
client: AsyncIOMotorClient | None = None
async def connect():
    global client
    client = AsyncIOMotorClient(settings.mongo_uri)
    await init_beanie(database=client.autoguru, document_models=[Car])
async def close(): client.close()
