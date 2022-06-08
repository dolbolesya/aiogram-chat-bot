from bot import bot, dp
from aiogram import types


@dp.message_handler(commands=['reg'])
async def cmd_reg(message: types.Message):
    pass
