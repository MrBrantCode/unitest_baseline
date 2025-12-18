"""
QUESTION:
Write a function `flatten_and_filter(arr)` that takes a nested array of integers and lists as input, and returns a sorted list of integers that are divisible by both 2 and 3. The function should recursively flatten the input array, excluding non-integer elements, before filtering and sorting the result.
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