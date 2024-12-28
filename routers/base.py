from aiogram.filters.command import Command
from aiogram import Router, types

from managers.generator import generator
from core.logger import logger

base_router = Router()


@base_router.message(Command('start'))
@logger.log_message
async def cmd_start(message: types.Message):
    return await message.answer('Все мы потом будем гореть в аду \nНо сейчас нажми на /generate')


@base_router.message(Command('generate'))
@logger.log_message
async def cmd_generate(message: types.Message):
    return await message.answer(generator.run())


@base_router.message(Command('set_rules'))
@logger.log_message
async def cmd_set_rules(message: types.Message):
    return await message.answer('Not works now')
