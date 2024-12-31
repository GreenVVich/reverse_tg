from aiogram.filters.command import Command
from aiogram import Router, types

from app.managers.generator import generator

base_router = Router()


@base_router.message(Command('start'))
async def cmd_start(message: types.Message):
    return await message.answer('Все мы потом будем гореть в аду \nНо сейчас нажми на /generate')


@base_router.message(Command('generate'))
async def cmd_generate(message: types.Message):
    return await message.answer(generator.run())


@base_router.message(Command('set_rules'))
async def cmd_set_rules(message: types.Message):
    return await message.answer('Not works now')
