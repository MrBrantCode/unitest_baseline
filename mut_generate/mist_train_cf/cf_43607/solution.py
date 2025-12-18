"""
QUESTION:
Write a function `longest_increasing_subsequence(sequence)` that takes a list of integers as input and returns the length of the longest increasing subsequence within the given sequence. The function should only consider subsequences where each element is greater than the previous one.
"""

def longest_increasing_subsequence(sequence):
    length = len(sequence)
    longest_subsequence = [1] * length
    # Compute optimized LIS values in bottom up manner
    for i in range (1 , length):
        for j in range(0 , i):
            if sequence[i] > sequence[j] and longest_subsequence[i]< longest_subsequence[j] + 1 :
                longest_subsequence[i] = longest_subsequence[j]+1
    maximum = 0
    # Pick maximum of all LIS values
    for i in range(len(longest_subsequence)):
        maximum = max(maximum , longest_subsequence[i])
    return maximum