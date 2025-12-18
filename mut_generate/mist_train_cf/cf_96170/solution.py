"""
QUESTION:
Write a function `find_pairs` that takes an array of integers `arr` and a target sum `value` as input. The function should return a list of distinct pairs of integers from the array whose sum is equal to the given `value`. The function should be able to handle negative integers and zeros in the array.
"""

def find_pairs(arr, value):
    pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == value:
                pairs.append((arr[i], arr[j]))
    return pairs