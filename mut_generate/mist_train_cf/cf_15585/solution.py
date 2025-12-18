"""
QUESTION:
Write a function named `find_max_difference` that takes an array of integers as input and returns the maximum absolute difference between any two elements in the array. The function should have a time complexity of O(n^2) and a space complexity of O(1).
"""

def find_max_difference(arr):
    max_diff = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            diff = abs(arr[i] - arr[j])  
            if diff > max_diff:
                max_diff = diff
    return max_diff