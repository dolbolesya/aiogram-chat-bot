from bot import bot, dp
from aiogram import types



@dp.message_handler(commands=['kick'], commands_prefix='/!', is_chat_admin=True)
async def cmd_kick(message: types.Message):
    if not message.reply_to_message:
        await message.reply('Эта команда должна быть ответом на сообщение!')
        return

    if message.reply_to_message:
        await bot.kick_chat_member(
            chat_id=message.chat.id,
            user_id=message.reply_to_message.from_user.id
        )
