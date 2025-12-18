"""
QUESTION:
Write a function called `remove_even_divisible_by_3_and_5` that takes a list of unique integers as input. The function should remove the first even number that is divisible by both 3 and 5, if it exists, and return the updated list sorted in descending order. The input list must contain at least 5 elements.
"""

def remove_even_divisible_by_3_and_5(lst):
    return sorted([x for x in lst if x % 2 != 0 or (x % 3 != 0 and x % 5 != 0)], reverse=True)