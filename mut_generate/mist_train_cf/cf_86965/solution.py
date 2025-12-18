"""
QUESTION:
Create a function named `calculate_product` that takes two parameters: a list of numbers and an upper limit. The function should calculate the product of all numbers in the list, handling negative integers, float numbers, and zero values, and return the product if it is less than or equal to the specified upper limit. If the product exceeds the upper limit, the function should return an error message. The function should also check for and handle an empty input list and non-numeric values in the list, returning an error message in each case.
"""

def calculate_product(numbers, upper_limit):
    if not numbers:
        return "Error: Empty list"

    product = 1
    for num in numbers:
        if not isinstance(num, (int, float)):
            return "Error: Invalid input"
        product *= num
        if product > upper_limit:
            return "Error: Product exceeds upper limit"

    return product