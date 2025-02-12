from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.managers.generator import generator
from app.managers.regulator import regulator
from app.types.callbacks import MenuCB


def start_menu(used_rule: int = 1) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text='Generate', callback_data=MenuCB(use_rule=used_rule).pack())
    builder.button(text='Menu', callback_data=MenuCB(to_page=1, use_rule=used_rule).pack())
    builder.adjust(1)
    return builder.as_markup()


def generate_menu(used_rule: int = 1) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text='Generate new', callback_data=MenuCB(use_rule=used_rule).pack())
    builder.button(text='Menu', callback_data=MenuCB(to_page=1, use_rule=used_rule).pack())
    builder.adjust(1)
    return builder.as_markup()


def menu_menu(used_rule: int = 1) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text='Arena', callback_data=MenuCB(use_rule=used_rule).pack())
    builder.button(text='Settings', callback_data=MenuCB(to_page=2, use_rule=used_rule).pack())
    builder.button(text='Donate', callback_data=MenuCB(use_rule=used_rule).pack())
    builder.button(text='Back', callback_data=MenuCB(to_page=0, use_rule=used_rule).pack())
    builder.adjust(1)
    return builder.as_markup()


def settings_menu(used_rule: int = 1) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text='Select rule', callback_data=MenuCB(to_page=3, use_rule=used_rule).pack())
    builder.button(text='Select random rule', callback_data=MenuCB(use_rule=generator.random_rule()).pack())
    builder.button(text='Back', callback_data=MenuCB(to_page=1, use_rule=used_rule).pack())
    builder.adjust(1)
    return builder.as_markup()


def rules_menu(used_rule: int = 1) -> InlineKeyboardMarkup:  # TODO
    builder = InlineKeyboardBuilder()
    for item in regulator.get_rule_list():
        builder.button(text=item.name, callback_data=MenuCB(use_rule=item.id))
    builder.button(text='Back', callback_data=MenuCB(to_page=2, use_rule=used_rule).pack())
    builder.adjust(1)
    return builder.as_markup()


def one_rule_menu(used_rule: int = 1) -> InlineKeyboardMarkup:  # TODO
    builder = InlineKeyboardBuilder()
    builder.button(text='Choose', callback_data='')
    builder.button(text='Share', callback_data='')
    builder.button(text='Back', callback_data=MenuCB(to_page=3, use_rule=used_rule).pack())
    builder.adjust(1)
    return builder.as_markup()


pages = [start_menu, menu_menu, settings_menu, rules_menu, one_rule_menu]
