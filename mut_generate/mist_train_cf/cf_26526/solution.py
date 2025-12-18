"""
QUESTION:
Implement the `calculate_profit_loss` function, which takes a list of stock trading commands as input and returns the total profit or loss after executing all trades. Each command is a tuple containing a stock symbol, a transaction type ("BUY" or "SELL"), and the quantity of shares traded. The stock prices are determined by the order of the commands. Assume the input trades are valid, with a matching SELL transaction for each BUY transaction. 

The function should calculate the total cost from BUY transactions and the total revenue from SELL transactions, then return their difference as the profit or loss.
"""

from typing import List, Tuple

def calculate_profit_loss(trades: List[Tuple[str, str, int]]) -> int:
    total_cost = 0
    total_revenue = 0
    inventory = {}
    
    for stock, transaction, quantity in trades:
        if transaction == "BUY":
            if stock in inventory:
                inventory[stock] += quantity
            else:
                inventory[stock] = quantity
            total_cost -= quantity  
        elif transaction == "SELL":
            inventory[stock] -= quantity
            total_revenue += quantity  
            
    profit_loss = total_revenue + total_cost  
    return profit_loss