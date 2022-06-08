# coding: utf-8
from flask import Flask()
from flask_restful import Api, Resource, reqparse
import logging


from aiogram import executor, types
from bot import dp, bot
from utils.notify import on_startup, on_shutdown
import handlers
from filters import IsAdminFilter


dp.filters_factory.bind(IsAdminFilter)

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown
    )
