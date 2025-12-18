"""
QUESTION:
Write a function `multiply_abs_values` that takes a list of numbers as input and returns the product of the absolute integer values of all numbers in the list, excluding any numbers whose absolute value exceeds 100.
"""

def multiply_abs_values(lst):
    result = 1
    for num in lst:
        if abs(num) <= 100:
            result *= abs(int(num))
    return result