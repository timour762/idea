from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from sqlalchemy import select

from database import SessionLocal
from models import User, Profile

router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):
    telegram_user = message.from_user

    async with SessionLocal() as session:
        result = await session.execute(
            select(User).where(User.telegram_id == telegram_user.id)
        )
        user = result.scalar_one_or_none()

        if user:
            await message.answer("Вы уже зарегистрированы ")
            return

        user = User(
            telegram_id=telegram_user.id,
            username=telegram_user.username,
            first_name=telegram_user.first_name,
            last_name=telegram_user.last_name,
)

        session.add(user)
        await session.commit()

    await message.answer("Пользователь зарегистрирован в таблице users ")


@router.message(Command("pro"))
async def pro_handler(message: Message):
    telegram_user = message.from_user

    async with SessionLocal() as session:
        result = await session.execute(select(User).where(User.telegram_id == telegram_user.id))
        user = result.scalar_one_or_none()

        if not user:
            await message.answer("Сначала выполните команду /start")
            return

        result = await session.execute(select(Profile).where(Profile.user_id == user.id))
        profile = result.scalar_one_or_none()

        if profile:
            await message.answer("Ваш профиль уже зарегистрирован ")
            return

        profile = Profile(user_id=user.id)
        session.add(profile)
        await session.commit()

    await message.answer("Профиль зарегистрирован в таблице profile ")
