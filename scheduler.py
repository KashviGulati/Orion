from apscheduler.schedulers.background import BackgroundScheduler
from agent_runner import autonomous_check_with_context
from telegram_bot import send_message   # you'll create this

def daily_check():
    result = autonomous_check_with_context()
    send_message(result)

scheduler = BackgroundScheduler()
scheduler.add_job(daily_check, 'interval', hours=24)

scheduler.start()