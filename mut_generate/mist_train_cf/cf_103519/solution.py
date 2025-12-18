"""
QUESTION:
Write a function `find_sum(arr)` that calculates the sum of all elements in the given array `arr` using a constant amount of space and with a time complexity of O(n), where n is the number of elements in `arr`. The function should handle the case where the input array is empty.
"""

def find_sum(arr):
    if not arr:
        return 0
    
    total = arr[0]
    n = len(arr)
    
    for i in range(1, n):
        total += arr[i]
        
    return total