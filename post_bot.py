import requests
import os
from dotenv import load_dotenv

load_dotenv()

def post_to_telegram(message):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
        print(f"✅ Posted: {message}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to post: {e}")

