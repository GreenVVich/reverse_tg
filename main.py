import asyncio

from core.bot import bot
from core.dispatcher import dp
from core.logger import logger


async def main():
    logger.log_start()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
