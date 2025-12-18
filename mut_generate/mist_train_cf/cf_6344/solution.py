"""
QUESTION:
Write a function `product_of_odd_numbers` that takes a list of integers as input and returns the product of all odd numbers greater than 10 and less than 20, rounded to the nearest integer. The function should be implemented recursively and should not use any loops. The function should have an optional second parameter for the product, defaulting to 1.
"""

def product_of_odd_numbers(numbers, product=1):
    if not numbers:
        return round(product)
    elif 10 < numbers[0] < 20 and numbers[0] % 2 != 0:
        return product_of_odd_numbers(numbers[1:], product * numbers[0])
    else:
        return product_of_odd_numbers(numbers[1:], product)