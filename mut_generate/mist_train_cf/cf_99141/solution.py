"""
QUESTION:
Create a function `calculate_total` that calculates the total cost of a purchase with discounts applied. The function should take three parameters: `user`, `items_list`, and `discount_code`. The function should have access to a dictionary `items` that maps item names to prices, and a dictionary `discounts` that maps discount codes to their corresponding percentage off. The function should update the user's purchase history and return the total cost.
"""

def calculate_total(user, items_list, discount_code=None):
    items = {
        "item1": 10,
        "item2": 20,
        "item3": 30
    }
    discounts = {
        "CODE1": 10,
        "CODE2": 20,
        "CODE3": 30
    }
    total = 0
    for item in items_list:
        total += items[item]
    if discount_code:
        total *= (100 - discounts[discount_code])/100
    return total