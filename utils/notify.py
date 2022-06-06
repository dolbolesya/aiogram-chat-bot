from bot import bot, dp
from data.config import TEST_CHANNEL_ID as chat_id
import logging


async def on_startup(_):
    try:
        await bot.send_message(
            chat_id=chat_id,
            text='Bot started'
        )
    except Exception as err:
        logging.exception(err)
        await bot.send_message(
            chat_id=chat_id,
            text=logging.exception(err)
        )
    from utils.set_bot_cmd import set_default_cmd
    await set_default_cmd(dp)


async def on_shutdown(_):
    try:
        await bot.send_message(
            chat_id=chat_id,
            text='Bot stopped'
        )
    except Exception as err:
        logging.exception(err)
        await bot.send_message(
            chat_id=chat_id,
            text=logging.exception(err)
        )
