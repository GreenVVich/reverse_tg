from typing import Callable, Dict, Awaitable, Any

from aiogram import BaseMiddleware
from aiogram.types import Message

from app.core.logger import Logger
from app.core.settings import settings


class LoggingMiddleware(BaseMiddleware):
    logger: Logger = Logger('MessageLogger', 'logs/' + settings.LOGS_FILE + '.log')

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Callable[[Message, Dict[str, Any]], Awaitable[Any]]:
        response = await handler(event, data)
        if isinstance(response, Message):
            self.logger.logger.info(
                f'message - {event.from_user.username} - {repr(event.text)[1:-1]} - {repr(response.text)[1:-1]}')

        return response
