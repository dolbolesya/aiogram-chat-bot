from bot import bot, dp
from aiogram import types


# not work
"""
@dp.message_handler(content_types=types.ContentTypes.VIDEO_CHAT_STARTED)
async def event_video_chat_started(message: types.Message):
    await message.delete()
    await bot.send_message(
        chat_id=message.chat.id,
        text=f'In {message.chat.title} started videochat'\
        'to connect chat touch button on title'
    )
"""