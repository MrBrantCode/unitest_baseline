"""
QUESTION:
Write a function named `find_missing_element` that takes an array of integers from 1 to 100 as input. The array may contain duplicate elements. The function should return the missing element(s) from the array while accounting for duplicates.
"""

def find_missing_element(arr):
    seen = set()
    full_set = set(range(1, 101))  # assuming the range is from 1 to 100
    for num in arr:
        if num in seen:
            seen.discard(num)
        else:
            seen.add(num)
    
    return full_set - seen