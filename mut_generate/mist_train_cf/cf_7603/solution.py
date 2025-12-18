"""
QUESTION:
Implement a function named 'mean' that calculates the mean of a given 1D array 'arr' without using any built-in numpy functions or methods. The function should handle the case where 'arr' is empty and return None in such cases. The implementation should have a time complexity of O(n) and a space complexity of O(1).
"""

def mean(arr):
    if len(arr) == 0:
        return None
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum / len(arr)