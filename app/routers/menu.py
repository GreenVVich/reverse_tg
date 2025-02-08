import json

from aiogram import Router, F
from aiogram.types import CallbackQuery

from app.types.callbacks import MenuCB
from app.keyboards.menu import pages, generate_menu
from app.managers.generator import generator
from app.managers.regulator import regulator

menu_router = Router()

# TODO handle not like that. Bug: if no to_page - go to generate


@menu_router.callback_query(MenuCB.filter(F.to_page.is_not(None)))
async def handle_menu(callback_query: CallbackQuery, callback_data: MenuCB):
    await callback_query.message.edit_text(text=f'{callback_data}',  # TODO Correct description of menu
                                           reply_markup=pages[callback_data.to_page](callback_data.use_rule))


@menu_router.callback_query(MenuCB.filter(F.use_rule.is_not(None)))
async def handle_generate(callback_query: CallbackQuery, callback_data: MenuCB):
    await callback_query.message.edit_text(text=generator.run(callback_data.use_rule),
                                           reply_markup=generate_menu(callback_data.use_rule))


@menu_router.callback_query()  # For debug
async def handle_callbacks(callback_query: CallbackQuery):
    cq = callback_query.model_dump(mode='JSON')
    print(json.dumps(cq, indent=4))

