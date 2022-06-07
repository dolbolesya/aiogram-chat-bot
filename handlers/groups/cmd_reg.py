from bot import bot, dp
from aiogram import types
from data.config import TEST_CHANNEL_ID as chat_id

@dp.message_handler(commands=['reg'])
async def cmd_reg(message: types.Message):
    pass


