"""
QUESTION:
Create a function named `calculate_product` that takes a list of numbers and an upper limit as parameters. The function should calculate the product of all numbers in the list and return it if the product does not exceed the upper limit. The function should handle negative integers, float numbers, and zero values in the list. It should also return an error message if the input list is empty, if the list contains non-numeric values, or if the product exceeds the upper limit.
"""

def calculate_product(numbers, upper_limit):
    if not numbers:
        return "Error: Empty list"

    product = 1
    for num in numbers:
        if isinstance(num, int) or isinstance(num, float):
            product *= num
        else:
            return "Error: Invalid input"

        if product > upper_limit:
            return "Error: Product exceeds upper limit"

    return product