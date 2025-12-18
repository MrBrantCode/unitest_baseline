"""
QUESTION:
Write a function `check_product(numbers)` that checks whether the product of numbers in a list is even or not and identifies the index of the first odd number in the list. The function should round floating point numbers to the nearest integer before checking, handle large lists efficiently by avoiding unnecessary multiplications, and terminate early when possible. If there are no odd numbers, return -1 for the first odd index.
"""

def check_product(numbers):
    product = 1
    first_odd_index = -1
    for i, num in enumerate(numbers):
        num = round(num)
        if num % 2 != 0:
            if first_odd_index == -1:
                first_odd_index = i
            product *= num
            if product % 2 != 0:
                break
    is_even = product % 2 == 0
    return is_even, first_odd_index