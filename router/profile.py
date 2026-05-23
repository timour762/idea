from typing import Any, Coroutine

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from sqlalchemy import select

from database.database import SessionLocal
from database.tst import get_user_profiles
from database.user import User
from crud.profil import create_profile
from crud.profil import count_users

router = Router()



@router.message(Command("profile"))
async def cmd_profile(message: Message) -> str:
    async with SessionLocal() as session:
        telegram_id = message.from_user.id
        username = message.from_user.username
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        number_of_users = await count_users()
        result = await create_profile(
            session=session,
            user_id=telegram_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            number_of_users=number_of_users
        )


    await message.answer(
        f"Твой профиль:\n"
        f"id: {result.user_id}\n"
        f"username: {result.username}\n"
        f"имя: {result.first_name}\n"
        f"фамилия: {result.last_name}"
    )

    data = await get_user_profiles(session)
    return f"users:{data}"