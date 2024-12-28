import logging
from aiogram import types

from core.settings import settings


class Logger:
    def __init__(self, name: str = 'logger', log_file: str = 'unexpected.log'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

    def log_start(self):
        self.logger.info('STARTED')

    def log_message(self, func):
        async def wrapper(message: types.Message):
            response = await func(message)
            self.logger.info(f'message - {message.from_user.username} - {repr(message.text)[1:-1]} - {repr(response.text)[1:-1]}')
            return response
        return wrapper


logger = Logger('BaseLogger', 'logs/' + settings.LOGS_FILE + '.log')
