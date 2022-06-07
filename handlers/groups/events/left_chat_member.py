from bot import bot, dp
from aiogram import types


@dp.message_handler(content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def event_leave_chat_member(message: types.Message):
    await message.delete()
    await bot.send_message(
        chat_id=message.chat.id,
        text=f'Bye {message.from_user.first_name} from {message.chat.title}'
    )
