from aiogram import Bot, Dispatcher, types
from data.config import BOT_TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(
    token=BOT_TOKEN,
    parse_mode=types.ParseMode.HTML,
)

storage = MemoryStorage(

)

dp = Dispatcher(
    bot,
    storage=storage
)
