"""
QUESTION:
Implement a recursive function named `product_of_odd_numbers` that takes a list of numbers and an initial product value as parameters, and returns the rounded product of all the odd numbers greater than 10 and less than 20 in the list.
"""

def product_of_odd_numbers(numbers, product=1):
    if not numbers:
        return round(product)
    elif 10 < numbers[0] < 20 and numbers[0] % 2 != 0:
        return product_of_odd_numbers(numbers[1:], product * numbers[0])
    else:
        return product_of_odd_numbers(numbers[1:], product)