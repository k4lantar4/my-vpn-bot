from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# بارگذاری متغیرهای محیطی از فایل .env
load_dotenv()

class Config(BaseSettings):
    BOT_TOKEN: str = os.getenv("BOT_TOKEN")

config = Config()
