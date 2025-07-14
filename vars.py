#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "22727464"))
API_HASH = environ.get("API_HASH", "f0e595a263c89aa17f6571b8af296ced")
BOT_TOKEN = environ.get("BOT_TOKEN", "7110231022:AAHzjuE3MR7FdUvdFnaEHKurmQ9526aTIiM")
OWNER = int(environ.get("OWNER", "887699812"))
CREDIT = environ.get("CREDIT", "STRANGER BOYS")
AUTH_USER = os.environ.get('AUTH_USERS', '887699812').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
