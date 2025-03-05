from aiogram import Router, types
from aiogram.filters import Command
from bot.database import add_user  # ایمپورت تابع ثبت کاربر

router = Router()

@router.message(Command("start"))
async def start_handler(message: types.Message):
    telegram_id = message.from_user.id
    username = message.from_user.username

    # ثبت کاربر در دیتابیس
    add_user(telegram_id, username)

    await message.answer("سلام! 👋 خوش آمدید.\nاطلاعات شما ثبت شد.")
