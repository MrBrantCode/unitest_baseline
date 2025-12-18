"""
QUESTION:
Write a function named `calculate_discount` that takes two parameters, `price` and `discount_percentage`, and returns the discounted price. The function should handle cases where the price is greater than or equal to zero and where the price is less than zero. Implement the function to achieve higher levels of statement and branch coverage. The function should handle the case where the price is exactly zero.
"""

def calculate_discount(price, discount_percentage):
    if price >= 0:
        discounted_price = price - (price * discount_percentage / 100)
    else:
        discounted_price = 0
    
    return discounted_price