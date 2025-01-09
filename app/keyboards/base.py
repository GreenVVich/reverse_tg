from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_base_commands_kb() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text='/generate')
    builder.button(text='/menu')
    builder.button(text='/help')
    builder.adjust(1)

    return builder.as_markup()
