"""
QUESTION:
Create a function `sum_and_extremes(lst)` that takes a list of integers as input and returns a tuple containing the sum of the list, the smallest number in the list, and the largest number in the list. The function should iterate through the list only once and update the minimum and maximum values as it calculates the sum.
"""

def sum_and_extremes(lst):
    total = 0
    min_val = max_val = lst[0]
    for i in lst:
        total += i
        if i < min_val:
            min_val = i
        elif i > max_val:
            max_val = i
    return (total, min_val, max_val)