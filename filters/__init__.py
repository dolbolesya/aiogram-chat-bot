from aiogram import Dispatcher
from .private_chat import is_private
from .public_chat import is_pablic

def setup(dp: Dispatcher):
    dp.filters_factory.bind(is_private)
    dp.filters_factory.bind(is_pablic)
