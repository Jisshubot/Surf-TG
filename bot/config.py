from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")


class Telegram:
    API_ID = int(getenv("API_ID"))
    API_HASH = getenv("API_HASH")
    BOT_TOKEN = getenv("BOT_TOKEN")
    PORT = int(getenv("PORT", "8080"))
    BASE_URL = getenv("BASE_URL").rstrip('/')
    AUTH_CHANNEL = [channel.strip()
                    for channel in getenv("AUTH_CHANNEL").split(",")]
    DATABASE_URL = getenv("DATABASE_URL")
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '10'))
    MULTI_CLIENT = bool(getenv('MULTI_CLIENT', 'False'))
