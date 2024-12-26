from aiogram import Dispatcher

from routers.base import base_router


dp = Dispatcher()

dp.include_routers(base_router)
