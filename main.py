import os
from telethon import TelegramClient, events
import requests

api_id = int(os.environ.get('API_ID'))
api_hash = os.environ.get('API_HASH')
phone = os.environ.get('PHONE')

N8N_WEBHOOK_URL = 'https://borhan2.app.n8n.cloud/webhook-test/news-webhook'

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

client = TelegramClient('yazd_news', api_id, api_hash)

@client.on(events.NewMessage(chats=CHANNELS))
async def handler(event):
    try:
        chat = await event.get_chat()
        text = event.message.message or "[پیام بدون متن]"
        link = f"https://t.me/{chat.username}/{event.message.id}" if chat.username else ""

        payload = {
            "channel": chat.title,
            "username": chat.username,
            "text": text,
            "link": link,
            "date": event.message.date.strftime('%Y-%m-%d %H:%M:%S')
        }
        requests.post(N8N_WEBHOOK_URL, json=payload, timeout=10)
        print(f"ارسال شد → {chat.title}")

    except Exception as e:
        print("خطا:", e)

async def main():
    print("در حال اتصال به تلگرام...")
    await client.start(phone)
    print("اتصال موفق! ۱۰ کانال خبری یزد و سراسری ۲۴/۷ در حال مانیتور شدن")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
