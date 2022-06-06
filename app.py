# coding: utf-8

import logging

logging.basicConfig(level=logging.DEBUG)
from aiogram import executor, types
from data.notify import on_startup, on_shutdown

if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_startup,
                           on_shutdown=on_shutdown)
