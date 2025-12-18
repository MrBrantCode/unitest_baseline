"""
QUESTION:
Construct a function `net_price(base_cost, discount, tax, quantity)` that calculates the net price of a product considering its base cost, applied discount percentage, additional taxation rate, and bulk pricing where every 5th product carries an additional 2% discount. The function should return the total net price for the given quantity of products.
"""

def calculate_net_price(base_cost, discount, tax, quantity):
    total_discount = discount
    if quantity % 5 == 0:
        total_discount += 2
    price_after_discount = base_cost * (1 - total_discount / 100)
    final_price = price_after_discount * (1 + tax / 100)
    return final_price * quantity