"""
QUESTION:
Write a function `multiply_abs_values(lst)` that takes a list of numbers as input and returns the product of the absolute values of the numbers in the list after rounding each number down to the nearest integer. The function should raise an exception if the length of the input list exceeds 10 or if the list contains more than one zero.
"""

from math import floor

def multiply_abs_values(lst):
    if len(lst) > 10 or lst.count(0) > 1:
        raise Exception("List length should not exceed 10 or contain more than one zero.")
    product = 1
    for num in lst:
        product *= abs(floor(num))
    return product