# telegram_bot.py

import asyncio
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

from agent_setup import agent

TOKEN = "8655778714:AAGChvxCLAMMOTkwHkX5gmsrWKQi6vUFJgU"
CHAT_ID = None  # will capture dynamically

# ✅ Async-safe wrapper for agent
async def run_agent(user_input):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, agent.run, user_input)

# ✅ Message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global CHAT_ID

    CHAT_ID = update.effective_chat.id  # store chat id

    user_input = update.message.text

    try:
        response = await run_agent(user_input)
    except Exception as e:
        response = f"Error: {str(e)}"

    await update.message.reply_text(response)

# ✅ Reusable send function (for scheduler)
bot_instance = Bot(token=TOKEN)

def send_message(text):
    if CHAT_ID:
        bot_instance.send_message(chat_id=CHAT_ID, text=text)

# ✅ App setup
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

if __name__ == "__main__":
    print("Bot is running...")
    app.run_polling()