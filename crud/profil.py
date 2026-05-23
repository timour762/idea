from sqlalchemy import delete, select, update
from  sqlalchemy.ext.asyncio import AsyncSession
from  database.profil import Profile
from sqlalchemy import select, func
from database.database import SessionLocal
from database.user import User

async def create_profile(
    session: AsyncSession,
    user_id: int,
    username: str,
    first_name: str,
    last_name: str,) ->Profile:
    user = await session.execute(
        select(Profile).where(Profile.user_id == user_id)
    )
    r = user.scalar_one_or_none()
    if r:
        return r

    profile= Profile(
        user_id=user_id,
        username=username,
        first_name=first_name,
        last_name=last_name
    )

    session.add(profile)
    await session.commit()
    await session.refresh(profile)
    return profile


async def get_profile(session: AsyncSession, user_id: int):
    result = await session.execute(
        select(Profile).where(Profile.user_id == user_id)
        )
    return result.scalar_one_or_none()

async def delete_profile(session: AsyncSession, user_id: int):
    result = await session.execute(
        delete(Profile).where(Profile.user_id == user_id)
        )
    await session.commit()
    return result.rowcount > 0


async def count_users():
    async with SessionLocal() as session:
        # Считаем количество записей
        result = await session.execute(select(func.count()).select_from(User))
        count = result.scalar()
        print(f"Всего пользователей: {count}")
        return count