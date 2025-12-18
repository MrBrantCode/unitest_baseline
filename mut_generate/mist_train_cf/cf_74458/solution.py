"""
QUESTION:
Write a function `prvPermOpt1(arr)` that takes an array of positive integers `arr` as input and returns the lexicographically largest permutation that is smaller than `arr` with exactly one swap, along with the indices of the swapped elements. If no swap is possible, return the original array and an empty array for the indices.

The length of `arr` is between 2 and 10^4 (inclusive), and each element in `arr` is between 1 and 10^4 (inclusive).
"""

def prvPermOpt1(arr):
    i = len(arr) - 2
    while i >= 0 and arr[i] <= arr[i+1]: i -= 1
    if i == -1: return arr
    j = len(arr) - 1
    while arr[j] >= arr[i]: j -= 1
    while arr[j] == arr[j-1]: j -= 1
    arr[i], arr[j] = arr[j], arr[i]
    return arr