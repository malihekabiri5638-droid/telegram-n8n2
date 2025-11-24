# telegram-n8n2
import os
from telethon import TelegramClient, events
import requests
api_id = int(os.environ.get('API_ID'))
api_hash = os.environ.get('API_HASH')
phone = os.environ.get('PHONE')
# main.py
import os
from telethon import TelegramClient, events
import requests

# از متغیرهای Railway می‌خونه (امن و مخفی)
api_id = int(os.environ.get('API_ID'))
api_hash = os.environ.get('API_HASH')
phone = os.environ.get('PHONE')

# وب‌هوک n8n تو
N8N_WEBHOOK_URL = 'https://borhan2.app.n8n.cloud/webhook-test/news-webhook'

# ۱۰ کانال خبری یزد و سراسری
CHANNELS = [
    'https://t.me/isnayazd24',
    'https://t.me/yazdiam',
    'https://t.me/yazdrasa',
    'https://t.me/yazdiribnews',
    'https://t.me/YazdFars',
    'https://t.me/snntv',
    'https://t.me/mehrnews',
    'https://t.me/isna94',
    'https://t.me/iribnews',
    'https://t.me/farsna'
]

client = TelegramClient('yazd_news_session', api_id, api_hash)

@client.on(events.NewMessage(chats=CHANNELS))
async def handler(event):
    try:
        chat = await event.get_chat()
        text = event.message.message or "[پیام رسانه‌ای]"
        link = f"https://t.me/{chat.username}/{event.message.id}" if hasattr(chat, 'username') and chat.username else ""

        payload = {
            "channel": chat.title,
            "username": getattr(chat, 'username', None),
            "text": text,
            "link": link,
            "date": event.message.date.strftime('%Y-%m-%d %H:%M:%S')
        }

        requests.post(N8N_WEBHOOK_URL, json=payload, timeout=10)
        print(f"ارسال شد → {chat.title}")

    except Exception as e:
        print("خطا:", e)

async def main():
    print("در حال اتصال به تلگرام با شماره", phone)
    await client.start(phone)
    print("اتصال موفق! مانیتورینگ ۱۰ کانال خبری یزد و سراسری شروع شد (۲۴/۷)")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
