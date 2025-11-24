# telegram-n8n2
import os
from telethon import TelegramClient, events
import requests
api_id = int(os.environ.get('API_ID'))
api_hash = os.environ.get('API_HASH')
phone = os.environ.get('PHONE')
