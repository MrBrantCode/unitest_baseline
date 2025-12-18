"""
QUESTION:
Create a function called `max_product` that takes a list of numbers as input and returns the pair of numbers with the largest product. The function should handle cases where the input list has less than two elements, and return an error message in such cases.
"""

def max_product(lst):
    if len(lst) < 2:
        return ("List must have at least two elements")
    elif len(lst) == 2:
        return (lst[0], lst[1])
    else:
        sorted_lst = sorted(lst)
        return (sorted_lst[-1], sorted_lst[-2])