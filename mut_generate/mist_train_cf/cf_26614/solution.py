"""
QUESTION:
Implement a function `calculate_total_price` that takes four parameters: 
- `items`: a list of strings representing the items in the shopping cart, 
- `quantities`: a list of integers representing the quantities of the corresponding items, 
- `base_prices`: a dictionary where the keys are item names and the values are their base prices, 
- `discount_rules`: a dictionary where the keys are item names and the values are tuples representing the quantity threshold for the discount and the discount percentage. 

The function should return the total price of the shopping cart based on the provided inputs. The total price is calculated by applying the base price to each item, and if applicable, a discount based on the quantity of each item. 

The function should be able to handle any number of items, quantities, base prices, and discount rules.
"""

from typing import List, Dict, Tuple

def calculate_total_price(items: List[str], quantities: List[int], base_prices: Dict[str, float], discount_rules: Dict[str, Tuple[int, float]]) -> float:
    total_price = 0.0
    for item, quantity in zip(items, quantities):
        base_price = base_prices[item]
        if item in discount_rules and quantity >= discount_rules[item][0]:
            discounted_price = base_price * (1 - discount_rules[item][1] / 100) # corrected discount
            total_price += discounted_price * quantity
        else:
            total_price += base_price * quantity
    return total_price