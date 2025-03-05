from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# بارگذاری متغیرهای محیطی از فایل .env
load_dotenv()

class Config(BaseSettings):
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_USER: str = os.getenv("DB_USER", "vpn_user")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "pass123456")
    DB_NAME: str = os.getenv("DB_NAME", "vpn_bot")
    DB_PORT: int = int(os.getenv("DB_PORT", 3306))  # مقدار پیش‌فرض 3306

config = Config()
