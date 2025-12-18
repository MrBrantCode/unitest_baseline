"""
QUESTION:
Write a function named `puzzle_product(integer, decimal)` that takes a positive integer and a decimal number as input. The decimal number can be a float or a string with at most two decimal places. The function should prompt the user with a math puzzle related to the inputs, and only return the rounded product if the user correctly answers the puzzle. The product should be rounded up if it is negative, and rounded down if it is non-negative.
"""

import math
def entrance(integer, decimal):
    # Convert decimal to float if it's a string
    if isinstance(decimal, str):
        decimal = float(decimal)
    
    # Calculate product
    product = integer * decimal
    
    # Prompt user with math puzzle
    puzzle = f"What is the sum of {integer} and {decimal:.2f}?"
    answer = input(puzzle)
    
    # Check if answer is correct
    if float(answer) == integer + decimal:
        # Round up or down based on product value
        if product >= 0:
            return math.floor(product)
        else:
            return math.ceil(product)
    else:
        return "Error: Incorrect answer to math puzzle."