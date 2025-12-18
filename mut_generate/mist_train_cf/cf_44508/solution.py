"""
QUESTION:
Construct a function `recursive_multiply` that takes a list of numbers as an argument and returns the product of all numbers in the list, calculated in the order they appear in the list. If the list is empty, the function should return 1 (the multiplicative identity).
"""

def recursive_multiply(numbers, product=1):
    # Check if the list of numbers is empty
    if not numbers:
        return product
    else:
        # Multiply the first number in the list by the product
        product *= numbers[0]
        # Recursively call the function with the remainder of the list
        return recursive_multiply(numbers[1:], product)