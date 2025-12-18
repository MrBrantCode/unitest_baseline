"""
QUESTION:
Write a function called `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate elements removed, while preserving the original order of the elements. Do not use any built-in Python functions or libraries, and do not modify the original list.
"""

def remove_duplicates(lst):
    result = []
    seen = set()
    
    for num in lst:
        if num not in seen:
            result.append(num)
            seen.add(num)
    
    return result