import asyncio

from app.core.bot import bot
from app.core.dispatcher import dp
from app.core.logger import base_logger


async def main():
    base_logger.status('STARTED')
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
