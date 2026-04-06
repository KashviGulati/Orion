# messenger.py

import os
from dotenv import load_dotenv
from telegram import Bot

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = Bot(token=TOKEN)

CHAT_ID = None  # will be set from bot

def set_chat_id(chat_id):
    global CHAT_ID
    CHAT_ID = chat_id

def send_message(text):
    if CHAT_ID:
        bot.send_message(chat_id=CHAT_ID, text=text)