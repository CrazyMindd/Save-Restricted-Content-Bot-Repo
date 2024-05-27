#Join me at telegram @dev_gagan

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = "25274255" #config("API_ID", default=None, cast=int)
API_HASH = "02b2832c0e2cc02d8cf178c8a95a5d59" #config("API_HASH", default=None)
BOT_TOKEN = "7118086758:AAEhE-DY6GUqVm4Ews6OfLqqvLldVuRo7m4" #config("BOT_TOKEN", default=None)
SESSION = "AQGqa00Awft9PN8hoYwpWfcY7aFWDX7CfsAoret2pKfsiMib2cPwH7eflRYryxxf1BNIjznY4ubs-yAgeJ3ZqH4RHjt2j1usgERor3Zn8mQk6_M3wnVkUr9jXdiQwKlx96i-nihrUuGLsPdo_TALhJW8l53VD71yE0GWdDH1wepXLqP1f4JWJ7FI1xEQ6GKxdpiF9tYIYYzs8iMYckmq4IOEa6b8qh6EWx9W4FKN2AGpiaZqECb0OOAWgGFz6XBlh8XXk8XAF_Ws0Cl8l6kirGLWawm9ZBmuF4DFUPQveImnXPUybdhATi5PQ-2P_y75L43YW7N6wT5GLp8Kg9aPPrDBJFpcegAAAAGnbPQIAA" #config("SESSION", default=None)
FORCESUB = "saverestrictd" #config("FORCESUB", default=None)
AUTH = "7103902728" #config("AUTH", default=None)
SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
