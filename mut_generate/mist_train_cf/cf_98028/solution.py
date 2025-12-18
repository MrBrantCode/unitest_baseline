"""
QUESTION:
Create a function `sum_to_zero` that takes an array of integers as input and returns a set of unique pairs of integers that sum to zero. The function should handle both positive and negative numbers, and no duplicate pairs should be returned. The function should have a time complexity of O(nlogn) and a space complexity of O(n).
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