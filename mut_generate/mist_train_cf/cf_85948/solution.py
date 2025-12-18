"""
QUESTION:
Create a function `pairs_sum_to_zero` that accepts a list of integers as input and returns `True` if there are two distinct elements in the list that add up to zero, and `False` otherwise. The function must check all possible pairs of distinct elements in the list.
"""

def pairs_sum_to_zero(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == 0:
                return True
    return False