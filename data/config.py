import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
TEST_CHANNEL_ID = os.getenv("TEST_CHANNEL_ID")


SKIP_UPDATES = os.getenv("SKIP_UPDATES", False)
NUM_BUTTONS = os.getenv("NUM_BUTTONS", 5)
ENTRY_TIME = os.getenv("ENTRY_TIME", 300)
BAN_TIME = os.getenv("BAN_TIME", 30)

admins_id = [
    334443202
]
