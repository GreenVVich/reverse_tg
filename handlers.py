from aiogram.filters.command import Command
from aiogram import types

from dispatcher import dp
from generator import generator


@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer('Все мы потом будем гореть в аду \nНо сейчас нажми на /generate')


@dp.message(Command('generate'))
async def cmd_generate(message: types.Message):
    await message.answer(generator.generate())


@dp.message(Command('set_rules'))
async def cmd_set_rules(message: types.Message):
    await message.answer('')
