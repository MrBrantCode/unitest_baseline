"""
QUESTION:
Create a function `calculate_discount` that takes two parameters: `price` and `percentage`. The function should calculate the discounted price after applying the given percentage discount to the original price. The function should validate its inputs: `price` should be a positive number, and `percentage` should be between 0 and 100. If the inputs are invalid, the function should raise an exception.
"""

def calculate_discount(price: float, percentage: float = 10.0) -> float:
    """Given an original price and a discount rate, calculate the discounted price.

    Further, handle any exceptions for non-positive price, zero or negative percentage values, and if the percentage is greater than 100.
    
    Return the discounted price with the given percentage discount rate (This should be a positive number and should not exceed 100). 

    """
    # Validate input
    if price <= 0:
        raise Exception("Price should be a positive number.")
    if percentage <= 0 or percentage > 100:
        raise Exception("Percentage should be a positive number and should not exceed 100.")

    # Calculate discounted price
    try:
        discounted_price = price - price * (percentage / 100)
    except TypeError as e:
        raise Exception("TypeError occurred: ", e)

    return discounted_price