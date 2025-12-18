"""
QUESTION:
Create a function `calculate_product(numbers, upper_limit)` that takes a list of numbers and an upper limit as input. The function should calculate the product of all numbers in the list, handling negative integers, float numbers, and zero values. The function should also check if the product exceeds the specified upper limit. If the product exceeds the limit or if a zero value is encountered, return an error message. Otherwise, return the calculated product.
"""

def calculate_product(numbers, upper_limit):
    product = 1
    for num in numbers:
        if num == 0:
            return "Error: Zero value detected. Product is zero."
        product *= num
        if product > upper_limit:
            return "Error: Product exceeds the upper limit."
    return product