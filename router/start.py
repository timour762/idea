from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from sqlalchemy import select

from database.database import SessionLocal
from database.user import User
from crud.user import create_user
router = Router()



@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    telegram_id = message.from_user.id

    async with SessionLocal() as session:
        result = await create_user(session=session,telegram_id=telegram_id)


    await message.answer("Пользователь зарегистрирован в таблице users")
