from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from bot.config import config

# مقداردهی اولیه ربات و دیسپچر
bot = Bot(token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()
