import asyncio
from aiogram import Dispatcher
from bot.bot import dp, bot
from bot.handlers.start import router

async def main():
    dp.include_router(router)  # ثبت هندلرها
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
