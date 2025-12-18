"""
QUESTION:
Create a function called `unique_list` that takes a list of integers as input, removes any duplicate elements, and returns the resulting list. The function should preserve the original order of elements in the list.
"""

def unique_list(lst):
    seen = []
    for number in lst:
        if number not in seen:
            seen.append(number)
    return seen