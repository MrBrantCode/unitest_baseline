"""
QUESTION:
Write a function `find_max_difference_pair(A)` that takes an integer array `A` as input and returns a pair of elements that have the maximum absolute difference. The function should have a time complexity of O(n log n) and a space complexity of O(1), where n is the length of array A. The array A will always have at least two elements, and if there are multiple pairs with the same maximum absolute difference, any one of them can be returned.
"""

def find_max_difference_pair(A):
    A.sort()  # Sort the array in non-decreasing order
    min_element = A[0]  # Initialize min_element to the first element
    max_element = A[-1]  # Initialize max_element to the last element

    return [min_element, max_element]