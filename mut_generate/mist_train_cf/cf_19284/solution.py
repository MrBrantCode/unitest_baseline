"""
QUESTION:
Create a function named `calculate_total_cost` that takes three parameters: `item_price`, `tax_rate`, and `quantity`, and returns the total cost of an item. The total cost is calculated based on the item price, tax rate, and applicable discounts or surcharges. The function should apply a discount rate based on the quantity: 5% for 1-10 items, 10% for 11-20 items, and 15% for more than 20 items. If the quantity is less than 1, no discount should be applied.
"""

def calculate_total_cost(item_price, tax_rate, quantity):
    if quantity >= 1 and quantity <= 10:
        discount_rate = 0.05
    elif quantity >= 11 and quantity <= 20:
        discount_rate = 0.10
    elif quantity > 20:
        discount_rate = 0.15
    else:
        discount_rate = 0

    total_cost = (item_price * quantity) * (1 - discount_rate) * (1 + tax_rate)
    return total_cost