from bot import bot, dp
from aiogram import types


@dp.message_handler(content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
async def event_new_chat_member(message: types.Message):

    await message.delete()
    for new_member in message.new_chat_members:
        await bot.send_message(
            chat_id=message.chat.id,
            text=f'Welcome {new_member.first_name} in {message.chat.title}'
        )

