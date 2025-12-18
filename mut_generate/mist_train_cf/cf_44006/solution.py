"""
QUESTION:
Create a function named `check_fiscal_status` that takes a single argument `amount` representing a fiscal amount. The function should return a string indicating whether the amount represents an economic profit, a financial shortfall, or neither. The function should treat positive amounts as a profit, negative amounts as a loss, and zero as neither a profit nor a loss.
"""

def check_fiscal_status(amount):
    if amount > 0:
        return "Economic Profit"
    elif amount < 0:
        return "Financial Shortfall"
    else:
        return "Neither Economic Profit nor Financial Shortfall"