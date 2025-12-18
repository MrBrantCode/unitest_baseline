"""
QUESTION:
Implement the function `calculate_total_cost` that takes three parameters: `items`, `prices`, and `discount_codes`. The function should calculate the total cost of a customer's purchase after applying any applicable discounts.

- Parameters:
  - `items`: A list of strings representing the items purchased (1 <= len(items) <= 100).
  - `prices`: A list of floats representing the prices of the corresponding items in the `items` list (len(prices) == len(items)).
  - `discount_codes`: A list of strings representing the discount codes available (0 <= len(discount_codes) <= 10).
- Return value: A float representing the total cost after applying any applicable discounts.

The discount codes can be either "ITEM" followed by the 1-indexed position of the item to discount, or "SALE" followed by the percentage discount to apply to the total cost. If a discount code is not applicable to any item, it should be ignored.
"""

from typing import List

def calculate_total_cost(items: List[str], prices: List[float], discount_codes: List[str]) -> float:
    total_cost = sum(prices)

    for code in discount_codes:
        if code.startswith("ITEM"):
            item_index = int(code[4:]) - 1
            if 0 <= item_index < len(items):
                total_cost -= prices[item_index]
        elif code.startswith("SALE"):
            discount_percentage = int(code[4:]) / 100
            total_cost *= (1 - discount_percentage)

    return total_cost