from db import cursor, conn
import re

def add_expense(text):
    amount = re.findall(r'\d+', text)
    category = text.split("on")[-1].strip()

    if amount:
        cursor.execute(
            "INSERT INTO expenses (amount, category) VALUES (?, ?)",
            (int(amount[0]), category)
        )
        conn.commit()

        return f"Added ₹{amount[0]} to {category}"
    
    return "Could not parse expense"