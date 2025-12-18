"""
QUESTION:
Implement a function `mean(arr)` that calculates the mean of array `arr` from scratch without using any built-in numpy functions or methods. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the array. If the input array is empty, the function should return None.
"""

def mean(arr):
    if len(arr) == 0:
        return None
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum / len(arr)