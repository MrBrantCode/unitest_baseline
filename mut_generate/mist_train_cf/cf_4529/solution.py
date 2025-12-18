"""
QUESTION:
Create a function called `calculate_total_cost` that takes four parameters: `item_price`, `tax_rate`, `surcharge`, and `quantity`. This function should calculate the total cost of an item by applying a discount based on the quantity of items purchased and considering an additional constraint that no discount is applied if the item price is less than $10. The discount tiers are as follows: 5% for 1-10 items, 10% for 11-20 items, and 15% for more than 20 items. The function should return the total cost of the item.
"""

def calculate_total_cost(item_price, tax_rate, surcharge, quantity):
    if item_price < 10:
        discount = 0
    elif 1 <= quantity <= 10:
        discount = 0.05
    elif 11 <= quantity <= 20:
        discount = 0.1
    else:
        discount = 0.15
    
    total_cost = (item_price + surcharge) * (1 + tax_rate) * (1 - discount)
    return total_cost