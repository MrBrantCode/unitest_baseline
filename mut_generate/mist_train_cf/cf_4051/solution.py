"""
QUESTION:
Write a function find_max_difference_pair that takes an array of integers A as input and returns a pair of elements with the maximum absolute difference. The function should have a time complexity of O(n log n) and a space complexity of O(1). The input array A will always have at least two elements. If there are multiple pairs with the same maximum absolute difference, the function can return any one of them.
"""

def find_max_difference_pair(A):
    A.sort()  # Sort the array in non-decreasing order
    return [A[0], A[-1]]