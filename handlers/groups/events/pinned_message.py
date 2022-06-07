from bot import bot, dp
from aiogram import types



@dp.message_handler(content_types=types.ContentTypes.PINNED_MESSAGE)
async def event_pinned_message(message: types.Message):
    await message.delete()
    await bot.send_message(
        chat_id=message.chat.id,
        text=f'new pin message 🤔 by {message.from_user.full_name}'
    )
