"""
QUESTION:
Create a function called `is_critical` that takes a list of integers and an integer `k` as input. The function should return `True` if the number of elements in the list that are greater than or equal to `k` is greater than half the length of the list, and `False` otherwise.
"""

def is_critical(lst, k):
    return lst.count(k) + sum(1 for i in lst if i > k) > len(lst) / 2