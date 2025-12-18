"""
QUESTION:
Write a Python function named `calculate_total_spent` that takes a list of transactions and an optional format parameter. The transactions list is a collection of dictionaries, each with keys "amount" (float) and "currency" (string). The function should calculate the total amount spent from the transactions and return it as a string in the specified format. The supported formats are "USD", "EUR", and "JPY", with "USD" being the default format. The format rules are as follows: "USD" should be prefixed with a dollar sign ($) and have two decimal places, "EUR" should be suffixed with a euro sign (€) and have two decimal places, and "JPY" should be suffixed with a yen sign (¥) and have no decimal places.
"""

def calculate_total_spent(transactions: list, format: str = None) -> str:
    total_spent = sum(transaction["amount"] for transaction in transactions)
    
    if format == "USD":
        return f"${total_spent:.2f}"
    elif format == "EUR":
        return f"{total_spent:.2f}€"
    elif format == "JPY":
        return f"¥{int(total_spent)}"
    else:
        return f"${total_spent:.2f}"