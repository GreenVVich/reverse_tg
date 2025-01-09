from aiogram import Dispatcher

from app.routers.base import base_router
from app.routers.menu import menu_router
from app.middlewares.message_logger import LoggingMiddleware


dp = Dispatcher()

dp.include_routers(base_router, menu_router)

dp.message.middleware(LoggingMiddleware())
