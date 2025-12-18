"""
QUESTION:
Develop a function `calculate_final_price(price, discount)` that takes in the price of a product and a discount percentage, and returns the final price after applying the discount and the amount saved. The discount percentage should be applied to the price as a percentage of the original price. The function should return both the final price and the discounted amount.
"""

def calculate_final_price(price, discount):
    discounted_amount = price * discount / 100
    final_price = price - discounted_amount
    return final_price, discounted_amount