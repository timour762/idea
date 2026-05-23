from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.user import User
from database.profil import Profile

async def get_user_profiles(session: AsyncSession):
    stmt = (
        select(User,Profile)
        .join(User.profile)
    )

    result = await session.execute(stmt)
    rows = result.all()

    data = []
    for user, profil in rows:
        data.append(
            {
                'user_id': user.id,
                'profil': {
                    'id': profil.user_id,
                    'username': profil.username
                }
            }
        )
    return data