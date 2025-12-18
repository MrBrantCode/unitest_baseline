"""
QUESTION:
Write a function `flatten_and_filter` that takes an array of lists as input, which can contain multiple levels of nesting and non-integer elements. The function should return a sorted list of integers that are divisible by both 2 and 3.
"""

def flatten_and_filter(arr):
    result = []
    for elem in arr:
        if isinstance(elem, list):
            result.extend(flatten_and_filter(elem))
        elif isinstance(elem, int) and elem % 2 == 0 and elem % 3 == 0:
            result.append(elem)
    result.sort()
    return result