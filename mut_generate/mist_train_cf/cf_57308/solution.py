"""
QUESTION:
Construct a Python function `max_product_pair(lst)` that takes a list of integer values as input and returns a pair of elements with the highest product. The list should contain at least two elements; otherwise, the function should return `None`.
"""

from itertools import combinations

def max_product_pair(lst):
    if len(lst) < 2:
        return None
    max_product = float('-inf')
    max_pair = None
    for pair in combinations(lst, 2):
         product = pair[0] * pair[1]
         if product > max_product:
             max_product = product
             max_pair = pair
    return list(max_pair)