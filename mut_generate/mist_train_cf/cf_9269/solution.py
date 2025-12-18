"""
QUESTION:
Write a function `max_difference` that takes an array of integers as input and returns the maximum difference between two consecutive elements. The function should have a time complexity of O(n), where n is the length of the array, and a space complexity of O(1).
"""

def max_difference(arr):
    max_diff = float('-inf')
    for i in range(len(arr)-1):
        diff = abs(arr[i+1] - arr[i])
        if diff > max_diff:
            max_diff = diff
    return max_diff