from aiogram import types
from bot import bot, dp


async def set_default_cmd(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'start bot'),
        types.BotCommand('help', 'info'),
        types.BotCommand('reg', 'reg chat')
    ])
