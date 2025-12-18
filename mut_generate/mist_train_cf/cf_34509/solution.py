"""
QUESTION:
Implement a function named `calculate_total_cost` that calculates the total cost of a shopping cart after applying any applicable discounts. The function should take two parameters: `cart`, a list of tuples where each tuple contains the item name and its price, and `discount_codes`, a dictionary containing discount codes as keys and discount percentages as values. The function should return the total cost after applying the highest discount available.
"""

from typing import List, Tuple, Dict

def calculate_total_cost(cart: List[Tuple[str, float]], discount_codes: Dict[str, float]) -> float:
    total_cost = sum(item[1] for item in cart)
    discount = max(discount_codes.values(), default=0.0)
    total_cost -= (total_cost * (discount / 100))
    return total_cost