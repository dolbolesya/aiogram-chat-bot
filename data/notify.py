from bot import bot
from data.config import TEST_CHANNEL_ID as chat_id

async def on_startup(_):
    await bot.send_message(
        chat_id=chat_id,
        text='Bot started'
    )


async def on_shutdown(_):
    await bot.send_message(
        chat_id=chat_id,
        text='Bot stopped'
    )
