from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

class IsAdminFilter(BoundFilter):
    key = "is_chat_admin"

    def __init__(self, is_admin):
        self.is_admin = is_admin

    async def check(self, message: types.Message):
        member = await message.bot.get_chat_member(
            chat_id=message.chat.id,
            user_id=message.from_user.id
        )

        return member.is_chat_admin()