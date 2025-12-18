"""
QUESTION:
Implement a function `product_of_list(lst)` that takes a list of integers `lst` and returns their product using the `reduce()` function from the `functools` module. Do not use the built-in `math.prod()` function, any other product-computing functions, or explicit loops (e.g. `for`, `while`). The solution should have a time complexity of O(n), where n is the length of the input list.
"""

from functools import reduce

def product_of_list(lst):
    return reduce(lambda x, y: x * y, lst)