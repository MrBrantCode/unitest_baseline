"""
QUESTION:
Write a function `reverse_dict_and_compute_product(input_dict)` that takes a dictionary with distinct keys and non-zero, non-negative integer values, reverses the order of its keys, and returns a new dictionary where each value is the product of its original dictionary value and all previous dictionary values when keys are sorted in ascending order.
"""

from functools import reduce
import operator

def reverse_dict_and_compute_product(input_dict):
    sorted_keys = sorted(input_dict.keys())
    reverse_dict = {}
    for key in reversed(sorted_keys):
        values_to_multiply = [input_dict[k] for k in sorted_keys if k <= key]
        product = reduce(operator.mul, values_to_multiply, 1)
        reverse_dict[key] = product
    return reverse_dict