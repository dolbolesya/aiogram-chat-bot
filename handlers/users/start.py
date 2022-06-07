from bot import bot, dp
from aiogram import types
from filters import is_private


@dp.message_handler(text='/start', is_private=True)
async def cmd_start(message: types.Message):
    await message.answer('start')
