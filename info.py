import re
from os import environ, getenv
from typing import Set, Optional, List, Dict
from Script import script  # Custom script file with caption & other settings

# 🚀 Bot Session and Token Information
SESSION = environ.get('SESSION', 'Sujan_BotZ')  # Pyrogram client session name

API_ID = int(environ.get('API_ID', '25502576'))  # Telegram API ID
API_HASH = environ.get('API_HASH', 'f0f35dbb5b0081cdc8d3c9d5383c4628')  # Telegram API Hash
BOT_TOKEN = environ.get('BOT_TOKEN', '8020187926:AAHKh6eOIiW4MM5hvp6cYTBqGJsAJYnBz4Q')  # Telegram Bot Token

# 👑, Channels & Logs
BIN_CHANNEL = int(environ.get("BIN_CHANNEL", "-1001978535504"))  # File storage channel
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1001978535504"))  # General log channel
PREMIUM_LOGS = int(environ.get("PREMIUM_LOGS", "-1001978535504"))  # Premium user actions log
VERIFIED_LOG = int(environ.get("VERIFIED_LOG", "-1001978535504"))  # Verified user actions log
SUPPORT_GROUP = int(environ.get("SUPPORT_GROUP", "-1001978535504"))

# add admin IDs 11111 2222 3333 and add auth channel IDs -100XXX -100XXX -100XXX
ADMINS = list(map(int, environ.get('ADMINS', '5123039648').split()))  # List of admin user IDs
AUTH_CHANNEL = list(map(int, environ.get("AUTH_CHANNEL", "-1001861445521").split()))  # Allowed channels for authorization

# username add without @
OWNER_USERNAME = environ.get("OWNER_USERNAME", 'Sujan_Ch')  # Owner's username
BOT_USERNAME = environ.get("BOT_USERNAME", 'TGFileToLinkxBot')  # Bot's username

# 🔗 Channel & Support Links
CHANNEL = environ.get('UPDATE CHANNEL', 'https://t.me/Sujan_Ch')  # Updates channel
SUPPORT = environ.get('SUPPORT CHANNEL', 'https://t.me/Sujan_BotZ')  # Support group
HOW_TO_VERIFY = environ.get('HOW_TO_VERIFY', 'https://t.me/')  # Verification guide link
HOW_TO_OPEN = environ.get('HOW_TO_OPEN', 'https://t.me/')  # File access guide link

# ✅ Feature Toggles (True/False)
VERIFY = environ.get("VERIFY", False)  # Enable user verification
FSUB = environ.get("FSUB", True)  # Force Subscribe feature
ENABLE_LIMIT = environ.get("ENABLE_LIMIT", True)  # Enable file limits
BATCH_VERIFY = environ.get("BATCH_VERIFY", False)  # Verify files in batch
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', False))  # Enable channel shortlink creation
MAINTENANCE_MODE = environ.get("MAINTENANCE_MODE", False)  # Put bot in maintenance
PROTECT_CONTENT = environ.get('PROTECT_CONTENT', False)  # Enable content protection
PUBLIC_FILE_STORE = environ.get('PUBLIC_FILE_STORE', False)  # Public or private file visibility
BATCH_PROTECT_CONTENT = environ.get('BATCH_PROTECT_CONTENT', False)  # Batch file protection

# 🔗 Shortlink Configuration
SHORTLINK_URL = environ.get('SHORTLINK_URL')  # Shortener site
SHORTLINK_API = environ.get('SHORTLINK_API')  # API key for shortlink

# 💾 MongoDB Connection Information
DB_URL = environ.get('DATABASE_URI', "mongodb+srv://copakim927:copakim927@cluster0.j6qikzi.mongodb.net/?retryWrites=true&w=majority")  # MongoDB connection URI
DB_NAME = environ.get('DATABASE_NAME', "Sujan_BotZ")  # MongoDB database name

# 📸 all Media (Images)
QR_CODE = environ.get('QR_CODE')  # QR Code image
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")  # Verify success image
AUTH_PICS = environ.get('AUTH_PICS', 'https://graph.org/file/721cd57c154c7f2a2b992-2bb665f9732ff027af.jpg')  # Auth step image
PICS = environ.get('PICS', 'https://graph.org/file/366530995fd47a006743e-4b4d613a61e1feb9ce.jpg')  # Default info image
FILE_PIC = environ.get('FILE_PIC', 'https://graph.org/file/721cd57c154c7f2a2b992-2bb665f9732ff027af.jpg') # file image 

# 📝 File Captions
FILE_CAPTION = environ.get('FILE_CAPTION', f"{script.CAPTION}")  # Caption for single file
BATCH_FILE_CAPTION = environ.get('BATCH_FILE_CAPTION', f"{script.CAPTION}")  # Caption for batch files
CHANNEL_FILE_CAPTION = environ.get('CHANNEL_FILE_CAPTION', f"{script.CAPTION}")  # Caption for channel posts

# ⏱️ Time & Rate Limit Settings
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # Ping interval in seconds (20 minutes)
SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))  # Threshold for sleep delay
RATE_LIMIT_TIMEOUT = int(environ.get("RATE_LIMIT_TIMEOUT", "600"))  # Rate limit time (10 mins)
MAX_FILES = int(environ.get("MAX_FILES", "10"))  # Max files allowed per user
VERIFY_EXPIRE = int(environ.get('VERIFY_EXPIRE', 60))  # Time (in hours) after which verification expires

# ⚙️ Worker Configuration
WORKERS = int(getenv('WORKERS', '4'))  # Number of async workers
MULTI_CLIENT = False  # Enable multi-client handling (if needed)

# 🔧 App/Heroku Configuration
name = str(environ.get('name'))  # Project name
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))  # Heroku app name (optional)
else:
    ON_HEROKU = False

# 🌐 Server Settings
PORT = int(getenv('PORT', '8080'))  # Port for web server
NO_PORT = str(getenv("NO_PORT", True)).lower() in ("true", "1", "yes")  # Disable port in URL
HAS_SSL = str(getenv("HAS_SSL", True)).lower() in ("true", "1", "yes")  # Use HTTPS if True
BIND_ADDRESS = getenv("WEB_SERVER_BIND_ADDRESS", "0.0.0.0")  # Server bind address
FQDN = getenv("FQDN", "") or BIND_ADDRESS  # Full domain name or fallback to bind address
PORT_SEGMENT = "" if NO_PORT else f":{PORT}/"  # Port in URL if not disabled
PROTOCOL = "https" if HAS_SSL else "http"  # Protocol for URL
URL = f"{PROTOCOL}://{FQDN}{PORT_SEGMENT}"  # Final generated base URL
