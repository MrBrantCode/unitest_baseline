"""
QUESTION:
Create a function named `maxPairwiseProduct` that takes an array of integers as input and returns the maximum pairwise product of those numbers with a time complexity of O(n log n), where n is the length of the array.
"""

def maxPairwiseProduct(arr):
    arr.sort()  # Sorting the array in ascending order
    n = len(arr)
    return arr[n-1] * arr[n-2]  # Returning the maximum pairwise product