"""
QUESTION:
Find the minimum absolute difference between any two elements in an integer array A containing at least two elements, possibly with duplicates. Implement a function `min_absolute_difference(A)` that takes the array A as input and returns the minimum absolute difference. The solution should have a time complexity of O(n log n) and a space complexity of O(1).
"""

def min_absolute_difference(A):
    A.sort()
    min_diff = float('inf')
    for i in range(1, len(A)):
        diff = abs(A[i] - A[i-1])
        if diff < min_diff:
            min_diff = diff
    return min_diff