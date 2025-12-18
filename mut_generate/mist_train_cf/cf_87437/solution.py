"""
QUESTION:
Write a function called `add_two_numbers` that takes two integer arguments and returns their sum. If either argument is not an integer, return "Error: Both inputs must be integers". The function should only use basic arithmetic operations and not rely on any built-in functions or libraries for addition.
"""

def add_two_numbers(a, b):
    # Check if the inputs are integers
    if not isinstance(a, int) or not isinstance(b, int):
        return "Error: Both inputs must be integers"
    
    # Calculate the sum of the two numbers
    sum = a + b
    
    return sum