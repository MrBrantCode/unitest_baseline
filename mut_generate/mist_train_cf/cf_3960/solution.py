"""
QUESTION:
Find the minimum value in a given array with a time complexity of O(n^3 log n). The function name should be `find_minimum` and it should take one parameter, the input array `arr`.
"""

def find_minimum(arr):
    n = len(arr)
    minimum = float('inf')  # Initialize minimum to positive infinity
    
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                minimum = min(minimum, arr[k])  # Update minimum if a smaller value is found
    
    return minimum