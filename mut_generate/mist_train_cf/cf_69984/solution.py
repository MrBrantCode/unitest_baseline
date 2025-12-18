"""
QUESTION:
Create a function `min_product` that takes a list of integers as input. The function should return the minimum product of five non-consecutive integers in the list. The list is guaranteed to be sorted, but the function should be able to handle any sorted list. If the list has less than 5 elements, or less than 4 negative numbers and 1 positive number, the function should return 0.
"""

def min_product(lst):
    if len(lst) < 5 or sum(1 for i in lst if i < 0) < 4 or sum(1 for i in lst if i > 0) < 1:
        return 0
    lst.sort()
    # product of 5 smallest numbers
    prod1 = lst[0]*lst[1]*lst[2]*lst[3]*lst[4]
    # product of 4 largest negative numbers and largest number
    prod2 = lst[0]*lst[1]*lst[2]*lst[3]*lst[-1]
    return min(prod1, prod2)