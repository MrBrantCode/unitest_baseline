"""
QUESTION:
Write a function `get_product(tup, target_product)` that takes a tuple `tup` and a target product `target_product` as input and returns a tuple of elements from `tup` whose product equals `target_product`. The function should consider all possible combinations of elements in `tup`, including non-consecutive elements and elements in reverse order. If no such combination is found, the function should return `None`.
"""

import itertools

def get_product(tup, target_product):
    n = len(tup)
    for r in range(n + 1):
        for combination in itertools.combinations(tup, r):
            product = 1
            for num in combination:
                product *= num
            if product == target_product:
                return combination
    return None