from aiogram import Router, types
from aiogram.filters import Command
from bot.database import update_user, delete_user

router = Router()

@router.message(Command("edituser"))
async def edit_user_handler(message: types.Message):
    args = message.text.split()
    if len(args) < 3:
        await message.answer("❌ فرمت صحیح: `/edituser telegram_id new_username`")
        return

    telegram_id = args[1]
    new_username = args[2]

    update_user(telegram_id, new_username)
    await message.answer(f"✅ نام کاربری کاربر `{telegram_id}` به `{new_username}` تغییر یافت.")

@router.message(Command("deluser"))
async def delete_user_handler(message: types.Message):
    args = message.text.split()
    if len(args) < 2:
        await message.answer("❌ فرمت صحیح: `/deluser telegram_id`")
        return

    telegram_id = args[1]

    delete_user(telegram_id)
    await message.answer(f"✅ کاربر `{telegram_id}` حذف شد.")
