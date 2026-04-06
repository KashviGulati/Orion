# scheduler.py

from apscheduler.schedulers.background import BackgroundScheduler
from agent_runner import autonomous_check
from messenger import send_message

def run_autonomous_task():
    print("🔥 Running autonomous check...")  # DEBUG
    result = autonomous_check()
    print("Result:", result)
    send_message(result)

scheduler = BackgroundScheduler()

# ⏰ run every 6 hours (change later)
scheduler.add_job(run_autonomous_task, 'interval', minutes=1)

def start_scheduler():
    scheduler.start()