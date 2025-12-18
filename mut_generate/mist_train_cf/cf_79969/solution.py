"""
QUESTION:
Implement a function named `find_median` that takes two sorted arrays `arr1` and `arr2` as input and returns the median value of the combined array. The function should handle both cases where the length of the combined array is odd or even.
"""

def find_median(arr1, arr2):
    combined = sorted(arr1 + arr2)
    length = len(combined)
    if length % 2 == 0:  # if length is even
        return (combined[length // 2] + combined[length // 2 - 1]) / 2.0
    else:  # if length is odd
        return combined[length // 2]