from aiogram import Router, types
from aiogram.filters import Command
from bot.database import add_subscription, get_user_subscriptions
from datetime import datetime, timedelta

router = Router()

@router.message(Command("buy"))
async def buy_subscription_handler(message: types.Message):
    args = message.text.split()
    if len(args) < 2:
        await message.answer("❌ فرمت صحیح: `/buy plan_name`")
        return

    telegram_id = message.from_user.id
    plan = args[1]
    expires_at = datetime.now() + timedelta(days=30)  # مدت اعتبار ۳۰ روز

    add_subscription(telegram_id, plan, expires_at)
    await message.answer(f"✅ اشتراک پلن `{plan}` برای شما ثبت شد و تا `{expires_at.strftime('%Y-%m-%d')}` اعتبار دارد.")

@router.message(Command("mysub"))
async def my_subscription_handler(message: types.Message):
    telegram_id = message.from_user.id
    subscriptions = get_user_subscriptions(telegram_id)

    if not subscriptions:
        await message.answer("❌ شما هیچ اشتراکی ندارید.")
        return

    response = "📜 **اشتراک‌های شما:**\n\n"
    for sub in subscriptions:
        plan = sub["plan"]
        expires_at = sub["expires_at"].strftime("%Y-%m-%d")
        response += f"🔹 پلن: `{plan}` | ⏳ تاریخ انقضا: `{expires_at}`\n"

    await message.answer(response)
