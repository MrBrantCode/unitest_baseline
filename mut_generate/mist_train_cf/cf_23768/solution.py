"""
QUESTION:
Given a list of integers, write a function named `longest_increasing_subsequence` that returns the length of the longest increasing subsequence in the list. A subsequence is considered increasing if every element is greater than the previous one.
"""

def longest_increasing_subsequence(arr):
    n = len(arr)
    L = [1]*n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                L[i] = max(L[i], L[j] + 1)

    longest_length = 0
    for i in range(n):
        longest_length = max(longest_length, L[i])
    return longest_length