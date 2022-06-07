from aiogram import types
from bot import dp

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(f'{message.from_user.username} кібер злочинець, вкрав моє серденько')