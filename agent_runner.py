# agent_runner.py

from agent_setup import agent
from db import cursor

def get_spending_data():
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0] or 0
    return total


def autonomous_check():
    total = get_spending_data()

    prompt = f"""
    User has spent ₹{total} so far this month.

    Decide:
    - Is this overspending?
    - Should we alert the user?
    - Give a short message (1–2 lines max)
    """

    response = agent.run(prompt)
    return response