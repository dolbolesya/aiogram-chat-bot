from bot import bot, dp
from data.config import TEST_CHANNEL_ID as chat_id
import logging


async def on_startup(_):
    from utils.set_bot_cmd import set_default_cmd

    try:
        await bot.send_message(
            chat_id=chat_id,
            text='Bot started'
        )
    except Exception as err:
        logging.exception(err)
        await bot.send_message(
            chat_id=chat_id,
            text=err
        )

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
            text=err
        )
