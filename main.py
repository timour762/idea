import asyncio
import logging
from aiogram import Bot, Dispatcher

from core.config import BOT_TOKEN
from router.profile import router as profile_router
from router.start import router as start_router


async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(start_router)
    dp.include_router(profile_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
