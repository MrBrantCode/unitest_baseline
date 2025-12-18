"""
QUESTION:
Create a function `sum_to_zero` that takes a list of integers as input, including both positive and negative numbers, and returns a set of unique pairs of numbers that add up to zero. The function should not include duplicate pairs in the output.
"""

def sum_to_zero(arr):
    arr.sort()
    result = set()
    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] + arr[j] == 0:
            result.add((arr[i], arr[j]))
            i += 1
            j -= 1
        elif arr[i] + arr[j] < 0:
            i += 1
        else:
            j -= 1
    return result