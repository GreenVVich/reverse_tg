from aiogram.filters.command import Command
from aiogram.types import Message
from aiogram import Router

from app.managers.generator import generator
from app.keyboards.base import get_base_commands_kb
from app.keyboards.menu import start_menu, generate_menu

base_router = Router()


@base_router.message(Command('start'))
async def cmd_start(message: Message):
    return await message.answer('Я бот для метаисторических приколдесов \nУ меня нет особого описания \n... \n Жмай /menu',
                                reply_markup=get_base_commands_kb())


@base_router.message(Command('help'))
async def cmd_help(message: Message):
    return await message.answer('Просто нажми /menu')


@base_router.message(Command('generate'))
async def cmd_generate(message: Message):
    rule = generator.random_rule()
    return await message.answer(generator.run(rule), reply_markup=generate_menu(rule))


@base_router.message(Command('menu'))
async def cmd_menu(message: Message):
    return await message.answer('Меню:', reply_markup=start_menu())

