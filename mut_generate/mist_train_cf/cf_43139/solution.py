"""
QUESTION:
Write a function `calculate_total_spent` that takes a list of transactions as input, where each transaction is a tuple containing a user ID and the amount spent. The function should return a dictionary where the keys are the user IDs and the values are the total amounts spent by each user.
"""

from typing import List, Tuple, Dict

def calculate_total_spent(transactions: List[Tuple[str, float]]) -> Dict[str, float]:
    total_spent = {}
    for user, amount in transactions:
        if user in total_spent:
            total_spent[user] += amount
        else:
            total_spent[user] = amount
    return total_spent