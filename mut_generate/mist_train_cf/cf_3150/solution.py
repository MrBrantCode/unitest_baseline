"""
QUESTION:
Implement a function named `reverse_array(arr)` that reverses the input array `arr` in-place, without using any built-in functions or libraries that directly reverse the array, and without creating a new array. The function should have a time complexity of O(n) and handle arrays with duplicates efficiently without using any additional space.
"""

def reverse_array(arr):
    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    return arr