"""
QUESTION:
Implement a function called `is_odd_count` that takes a list of integers as input. The function should determine whether the list contains an odd number of odd integers and return a boolean value indicating this, along with the count of odd integers present in the list. The input list can contain positive and negative integers, duplicates, and be unsorted, but will always contain at least one integer.
"""

def is_odd_count(lst):
    odd_count = 0
    for num in lst:
        if num % 2 != 0:
            odd_count += 1
    return odd_count % 2 == 1, odd_count