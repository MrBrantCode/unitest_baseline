"""
QUESTION:
Implement a function `product_in_range_extended` that takes a list of integers `l` and a range defined by `min_val` and `max_val` as input. The function should return a tuple where the first element is a boolean indicating whether the product of all elements in the list falls within the defined range, and the second element is a list of integers from the input list for which the product of the rest of the elements (excluding the considered one) falls within the defined range. The function assumes that the input list does not contain zero to avoid division by zero errors.
"""

from functools import reduce
import operator

def product_in_range_extended(l: list, min_val: int, max_val: int):
    # get the product of all elements
    total_product = reduce(operator.mul, l, 1)
    # if the total product is not in range, then first part of result is False
    r_all_in_range = min_val <= total_product <= max_val
    # now we move on to the second part
    r_individuals_in_range = []
    for i in range(len(l)):
        # get the product excluding the ith element
        product_excluding_i = total_product // l[i]
        # if this product is in the range, add the ith element to the list
        if min_val <= product_excluding_i <= max_val:
            r_individuals_in_range.append(l[i])
    return r_all_in_range, r_individuals_in_range