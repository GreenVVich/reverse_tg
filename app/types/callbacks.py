from aiogram.filters.callback_data import CallbackData


class MenuCB(CallbackData, prefix='Menu'):
    use_rule: int = 1  # TODO UID
    to_page: int | None = None  # TODO ENUM
