"""
QUESTION:
Create a function called `calculate_product` that takes two inputs: a list of numbers and an upper limit. This function should calculate the product of all numbers in the list, handling both positive and negative integers, float numbers, and zero values. The function should return the product if it is within the specified upper limit; otherwise, it should return an error message.
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