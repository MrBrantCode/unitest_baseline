"""
QUESTION:
Design a function named `sumOfOddLengthSubarrays` that takes an array as input and returns the cumulative sum of all subarrays with an odd length. The function should optimize for both time and space complexity, ensuring efficiency when handling large datasets.
"""

def sumOfOddLengthSubarrays(arr):
    n = len(arr)
    total = 0

    for i in range(n):
        total += ((i+1)*(n-i) + 1) // 2 * arr[i]

    return total