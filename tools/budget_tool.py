from db import cursor

def check_budget():
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]

    if total is None:
        total = 0

    return f"Total spent so far: ₹{total}"