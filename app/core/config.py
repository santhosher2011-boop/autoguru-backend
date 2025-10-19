from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    mongo_uri: str
    redis_url: str
    cloudinary_cloud: str
    cloudinary_key: str
    cloudinary_secret: str
    openai_api_key: str
    jwt_secret_key: str
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 10080
settings = Settings()
