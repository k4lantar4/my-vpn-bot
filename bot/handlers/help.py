from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("help"))
async def cmd_help(message: types.Message):
    help_text = "🔹 **راهنمای ربات**\n\n"
    help_text += "/start - شروع ربات\n"
    help_text += "/help - نمایش راهنما\n"
    help_text += "/about - درباره ربات\n"
    
    await message.answer(help_text)
