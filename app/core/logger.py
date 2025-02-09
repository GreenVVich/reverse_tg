import logging
from aiogram import types

from app.core.settings import settings


class Logger:
    def __init__(self, name: str = 'logger', log_file: str = 'unexpected.log'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

    def status(self, status: str):
        self.logger.info(f'status - {status}')

    def info(self, message: str):
        self.logger.info(message)


base_logger = Logger('BaseLogger', 'logs/' + settings.LOGS_FILE + '.log')
