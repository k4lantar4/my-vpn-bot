from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
import asyncio
from bot.config import config
from bot.handlers.start import router as start_router
from bot.handlers.help import router as help_router
from bot.handlers.about import router as about_router
from bot.handlers.users import router as users_router
from bot.handlers.manage_users import router as manage_users_router
from bot.handlers.subscriptions import router as subscriptions_router

# مقداردهی اولیه ربات و دیسپچر
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()

# اضافه کردن هندلرهای مختلف
dp.include_router(start_router)
dp.include_router(help_router)
dp.include_router(about_router)
dp.include_router(users_router)
dp.include_router(manage_users_router)
dp.include_router(subscriptions_router)

# تابع برای اجرای ربات
async def main():
    print("🚀 Bot is running...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
