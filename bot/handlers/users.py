from aiogram import Router, types
from aiogram.filters import Command
from bot.database import get_users

router = Router()

@router.message(Command("users"))
async def list_users_handler(message: types.Message):
    users = get_users()

    if not users:
        await message.answer("❌ هنوز هیچ کاربری ثبت نشده است.")
        return

    response = "📋 **لیست کاربران ثبت‌شده:**\n\n"
    for user in users:
        telegram_id = user["telegram_id"]
        username = user["username"] if user["username"] else "نامشخص"
        created_at = user["created_at"].strftime("%Y-%m-%d %H:%M")
        response += f"🆔 `{telegram_id}` | 👤 {username} | 📅 {created_at}\n"

    await message.answer(response)
