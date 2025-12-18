"""
QUESTION:
Create a function named `square_pairs` that takes a list of positive integers as input. The function should return the total count of non-overlapping pairs of adjacent numbers in the list whose product is a perfect square. A perfect square is defined as a number whose square root is an integer.
"""

def entrance(lst):
    count = 0
    for i in range(len(lst) - 1):
        product = lst[i] * lst[i + 1]
        if (product ** 0.5).is_integer():
            count += 1
    return count