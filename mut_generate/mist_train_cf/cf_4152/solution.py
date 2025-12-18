"""
QUESTION:
Implement a function called `product_of_list` that takes a list of integers as input and returns the product of all the elements. You must use the `reduce` function from the `functools` module and a lambda function to achieve this, without using any loops or the built-in `math.prod()` function. The function should have a time complexity of O(n), where n is the length of the input list.
"""

from functools import reduce

def product_of_list(lst):
    return reduce(lambda x, y: x * y, lst)