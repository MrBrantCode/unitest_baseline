"""
QUESTION:
Write a function `max_product_of_three(lst)` that takes in a list of integers `lst` with at least 3 elements and returns the highest product that can be obtained by multiplying 3 integers from the list. The function should work correctly even if the list contains negative numbers or zeros.
"""

def max_product_of_three(lst):
    lst.sort()
    n = len(lst)
    return max(lst[0] * lst[1] * lst[n-1], lst[n-3] * lst[n-2] * lst[n-1])