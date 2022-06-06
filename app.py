# coding: utf-8

import logging
from aiogram import executor, types
from bot import dp, bot
from utils.notify import on_startup, on_shutdown

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown
    )
