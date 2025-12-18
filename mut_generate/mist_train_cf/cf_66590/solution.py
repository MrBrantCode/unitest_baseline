"""
QUESTION:
Create a function `sort_elements` that takes an array and a condition function `cond_fn` as input, sorts the array based on the condition function, and returns the sorted array if the following conditions are met:

- The length of the array is between 1 and 9000 (inclusive).
- Each element in the array is between 0 and 10000 (inclusive).
- The input is a list.
- The condition function `cond_fn` returns True when applied to a dictionary where keys are unique elements in the array and values are their corresponding counts.

If any of these conditions are not met, the function should return None. The time complexity of the function should be considered in its design.
"""

def sort_elements(array, cond_fn):
    if not (1 <= len(array) <= 9000) \
            or not all(0 <= el <= 10000 for el in array)\
            or not isinstance(array, list)\
            or not cond_fn({x: array.count(x) for x in set(array)}):
        return None
    return sorted(array)