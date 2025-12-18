"""
QUESTION:
Write a function named `third_smallest_distinct_even` that takes a list of integers as input. The function should return a tuple containing the 3rd smallest distinct even integer in the list and the cumulative product of all unique even numbers in the list. If there are less than 3 distinct even integers in the list, the function should return (None, None). The function must not use any built-in or library functions to calculate the cumulative product.
"""

def third_smallest_distinct_even(l: list):
    even_list = []
    product = 1
    for x in sorted(set(l)):
        if x % 2 == 0:
            even_list.append(x)
            product *= x
    if len(even_list) >= 3:
        return even_list[2], product
    else:
        return None, None