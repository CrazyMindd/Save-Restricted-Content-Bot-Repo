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
SESSION = "AQGqa00ATVmgTrEjvaATdr7ycQrco71cTx53MeY2eh1TljtJZ_9IiIhr5NaHqGg4uF4LN-XlH7mSasLqiRMOtylBlWbzkEw4zvJoPA6LDgtdlv2mpf-In_sHq818LlHP9sNOAc2IB76SBHM6MYPAvpI3ZeTzwQqMv7cAkk843vDdmbhAYjZQ_I8CExiDGi81aRaTMrA8JXazqKgCeBsuMlfntIUiTh3bznuM6QyR2hG5ueWlhLI93rfozGc11w_K4KZpTRuFYfscbgTvpiMLb9UudmtEtieLYbQwGy8xroai3ZabY8fctw7gc2bGVbKCOb0BH1ZCmv501D9Gs3KbewsHnG-5YgAAAAGnbPQIAA" #config("SESSION", default=None)
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
