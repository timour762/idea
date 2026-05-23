from sqlalchemy import delete, select, update
from  sqlalchemy.ext.asyncio import AsyncSession
from  database.user import User

async def create_user(
    session: AsyncSession,
    telegram_id: int,
) -> User:
    r = await session.execute(select(User).where(User.telegram_id == telegram_id))
    r2 = r.scalar_one_or_none()
    if r2:
        return r2

    user = User(telegram_id=telegram_id)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user

async def get_user(session: AsyncSession, telegram_id: int):
    result = await session.execute(
        select(User).where(User.telegram_id == telegram_id)
        )
    return result.scalar_one_or_none()

async def delete_user(session: AsyncSession, telegram_id: int):
    result = await session.execute(
        delete(User).where(User.telegram_id == telegram_id)
        )
    await session.commit()
    return result.rowcount > 0