"""
QUESTION:
Create a function `product_in_range` that takes a list `l` of integers, two ranges defined by `min_val` and `max_val`, an additional integer `add_val`, and another range defined by `sum_min_val` and `sum_max_val`. The function should return `True` if the sum of the product of all elements in `l` and `add_val` falls within the range `[min_val, max_val]`, and the sum of the digits of this sum falls within the range `[sum_min_val, sum_max_val]`. The function should have a time complexity of less than O(n^2).
"""

from functools import reduce

def product_in_range(l: list, min_val: int, max_val: int, add_val: int, sum_min_val: int, sum_max_val: int) -> bool:
    product = reduce((lambda x, y: x*y), l)
    sum_val = product + add_val
    if sum_val >= min_val and sum_val <= max_val:
        digit_sum = sum(map(int, str(sum_val)))
        if digit_sum >= sum_min_val and digit_sum <= sum_max_val:
            return True
    return False