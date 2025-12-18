"""
QUESTION:
Implement a function `calculate_total_price(cart: [(String, Float)], discount_code: String?) -> Float` that calculates the total price of items in a shopping cart, taking into account any discounts that may apply. The function should accept a list of tuples, where each tuple represents an item in the cart, containing the item name (a string) and its price (a float), and an optional discount code. If the discount code is "SAVE20", a 20% discount should be applied to the total price.
"""

def calculate_total_price(cart, discount_code):
    total_price = sum(item[1] for item in cart)
    
    if discount_code == "SAVE20":
        total_price *= 0.8  # Apply 20% discount
    
    return total_price