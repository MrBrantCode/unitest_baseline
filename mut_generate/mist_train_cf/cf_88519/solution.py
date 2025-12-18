"""
QUESTION:
Create a function `calculate_total_cost` that takes four parameters: `item_price`, `tax_rate`, `surcharge`, and `quantity`. The function should calculate the total cost of an item given the item price, tax rate, surcharge, and any applicable discounts based on the quantity purchased. The discounts are as follows: 
- 5% for quantities between 1 and 10, 
- 10% for quantities between 11 and 20, 
- 15% for quantities more than 20, 
- no discount if the item price is less than $10.
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