"""
QUESTION:
Implement the function `calculate_profit_loss(transactions: List[str]) -> float` that takes a non-empty list of well-formed transaction strings as input, where each transaction is in the format "action, quantity, purchase_price, selling_price, commission". The function should return the total profit or loss, with a positive value representing profit and a negative value representing loss. The action can be either "buy" or "sell", and the quantity, purchase price, selling price, and commission are all floating-point numbers.
"""

from typing import List

def calculate_profit_loss(transactions: List[str]) -> float:
    """
    Calculate the total profit or loss from a list of transactions.

    Args:
        transactions (List[str]): A list of transactions, where each transaction is a string in the format
            "action, quantity, purchase_price, selling_price, commission".

    Returns:
        float: The total profit or loss, with a positive value representing profit and a negative value representing loss.
    """
    total_profit_loss = 0.0
    for transaction in transactions:
        action, quantity, purchase_price, selling_price, commission = transaction.split(', ')
        quantity, purchase_price, selling_price, commission = (
            float(quantity),
            float(purchase_price),
            float(selling_price),
            float(commission)
        )
        if action == 'buy':
            total_profit_loss -= quantity * purchase_price + commission
        elif action == 'sell':
            total_profit_loss += quantity * selling_price - commission
    return total_profit_loss