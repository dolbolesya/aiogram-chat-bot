from bot import bot, dp
from aiogram import types
from filters import IsAdminFilter


@dp.message_handler(commands=['unban'], commands_prefix='/!',is_chat_admin=True)
async def cmd_unban(message: types.Message):
    if not message.reply_to_message:
        await message.reply('Эта команда должна быть ответом на сообщение!')
        return

    if message.reply_to_message:
        await bot.unban_chat_member(
            chat_id=message.chat.id,
            user_id=message.reply_to_message.from_user.id
        )

