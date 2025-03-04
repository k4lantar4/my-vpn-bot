from aiogram import Router, types
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("سلام! خوش آمدید 🎉")
