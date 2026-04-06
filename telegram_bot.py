# telegram_bot.py

import asyncio
import os
from dotenv import load_dotenv

from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from scheduler import start_scheduler

from agent_setup import agent

# ✅ Load env
load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = None

# ✅ Async-safe agent call
async def run_agent(user_input):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, agent.run, user_input)

# ✅ Handle incoming messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global CHAT_ID

    from messenger import set_chat_id

    set_chat_id(update.effective_chat.id)

    user_input = update.message.text

    try:
        response = await run_agent(user_input)
    except Exception as e:
        response = f"Error: {str(e)}"

    await update.message.reply_text(response)

# ✅ Bot instance for sending messages (autonomous use)
bot_instance = Bot(token=TOKEN)

def send_message(text):
    if CHAT_ID:
        bot_instance.send_message(chat_id=CHAT_ID, text=text)

# ✅ Start app
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

if __name__ == "__main__":
    start_scheduler()
    print("Bot is running...")
    app.run_polling()