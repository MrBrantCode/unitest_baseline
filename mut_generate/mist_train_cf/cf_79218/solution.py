"""
QUESTION:
Write a function `check_product` that takes a list of numbers as input and returns a tuple containing a boolean indicating whether the product of the numbers in the list is even, and the index of the first odd number encountered in the list. If the list contains no odd numbers, the function should return -1 for the index. The function should handle lists containing both integers and floating point numbers by rounding floating point numbers to the nearest integer, and should correctly handle negative numbers and zero.
"""

def check_product(numbers):
    for i in range(len(numbers)):
        num = round(numbers[i])
        if num == 0:
            return True, -1
        if num % 2 != 0:
            return False, i
    return True, -1