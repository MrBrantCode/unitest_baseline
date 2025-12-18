"""
QUESTION:
Write a function `find_pairs` that takes an array of integers `arr` and a target value `value` as input, and returns a list of distinct pairs of integers in the array whose sum is equal to `value`. The function should handle arrays containing negative integers and zeros.
"""

def find_pairs(arr, value):
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == value:
                pairs.append((arr[i], arr[j]))
    return pairs