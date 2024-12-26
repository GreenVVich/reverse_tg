from aiogram.filters.command import Command
from aiogram import Router, types

from core.settings import settings
from core.bot import bot
from managers.generator import generator

base_router = Router()


@base_router.message(Command('start'))
async def cmd_start(message: types.Message):
    username = message.from_user.username
    await bot.send_message(chat_id=settings.ADMIN_ID, text=f'New call: {username}')
    print(username)
    await message.answer('Все мы потом будем гореть в аду \nНо сейчас нажми на /generate')


@base_router.message(Command('generate'))
async def cmd_generate(message: types.Message):
    await message.answer(generator.run())


@base_router.message(Command('set_rules'))
async def cmd_set_rules(message: types.Message):
    await message.answer('')
