"""
QUESTION:
Create a function called `calculate_profit(company, buy_price, sell_price, quantity)` that calculates the profit or loss from buying and selling shares of a specific company. The function should take the name of the company, the buying price per share, the selling price per share, and the quantity of shares as arguments, and return the total profit (if positive) or loss (if negative) from the transaction. Assume the existence of `buy_shares` and `sell_shares` functions that handle the actual buying and selling of shares.
"""

def calculate_profit(company, buy_price, sell_price, quantity):
    total_cost = buy_price * quantity
    total_revenue = sell_price * quantity
    profit_loss = total_revenue - total_cost
    return profit_loss