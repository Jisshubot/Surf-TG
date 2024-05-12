from os import getenv


AUTH_CHANNEL = [channel.strip()for channel in getenv("AUTH_CHANNEL").split(",")]
THEME = getenv("THEME", "quartz")
USERNAME = getenv("USERNAME", "admin")
PASSWORD = getenv("PASSWORD", "admin")
ADMIN_USERNAME = getenv("ADMIN_USERNAME", "surfTG")
ADMIN_PASSWORD = getenv("ADMIN_PASSWORD", "surfTG")
