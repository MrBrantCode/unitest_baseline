"""
QUESTION:
Create a function `max_product_subset` that takes a list of integers as input and returns the maximum achievable multiplication result of a contiguous subset within the list. The input list can contain both positive and negative numbers, and the function should handle cases where the list is empty or contains zero.
"""

def max_product_subset(lst):
    if not lst: return 0
    max_prod, min_prod, result = lst[0], lst[0], lst[0]

    for i in range(1, len(lst)):
        if lst[i] < 0:
            max_prod, min_prod = min_prod, max_prod

        max_prod = max(lst[i], max_prod * lst[i])
        min_prod = min(lst[i], min_prod * lst[i])
        result = max(result, max_prod)

    return result