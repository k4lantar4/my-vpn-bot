from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("about"))
async def cmd_about(message: Message):
    about_text = "🤖 **ربات فروش V2Ray**\n\n"
    about_text += "📌 این ربات برای خرید و مدیریت اکانت‌های V2Ray طراحی شده است.\n"
    about_text += "💻 توسعه یافته توسط تیم حرفه‌ای.\n"
    
    await message.answer(about_text)
