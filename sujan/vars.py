# (c) adarsh-goel (c) @sujan
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()
bot_name = " Fɪʟᴇ2Lɪɴᴋ Bᴏᴛ"
sujan_channel = "https://telegram.me/Sujan_BotZ"
sujan_grp = "https://telegram.me/Sujan_BotZ"

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '20077744'))
    API_HASH = str(getenv('API_HASH', '64f8e1cce4c865e981a8000f4ae33820'))
    BOT_TOKEN = str(getenv('BOT_TOKEN' , '6986528172:AAHWOxTQ9oIbilQFDX8xm137kCArmQryTVo'))
    name = str(getenv('name', 'file2link_bot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002116090653'))
    NEW_USER_LOG = int(getenv('NEW_USER_LOG', '-1002116090653'))
    PORT = int(getenv('PORT', '8080'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "6474527080").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'Sujan_Bots'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME')) #dont need to fill anything here
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', 'BIND_ADRESS:PORT')) if not ON_HEROKU or getenv('FQDN', '') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',True))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://jeyesa3599:jeyesa3599@cluster0.aloblt2.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'Sujan_BotZ')) 
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001929954249")).split()))   
    BAN_CHNL = list(set(int(x) for x in str(getenv("BAN_CHNL", "-1001929954249")).split()))   
    
