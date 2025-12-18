"""
QUESTION:
Write a function `find_minimum_value(arr)` that finds the minimum value in a given array. The function should have a time complexity of O(n^2 log n), where n is the length of the array.
"""

def find_minimum_value(arr):
    n = len(arr)
    minimum = float('inf')  
    
    for i in range(n):
        for j in range(i+1, n):
            pair = sorted([arr[i], arr[j]])
            if pair[0] < minimum:
                minimum = pair[0]
    
    return minimum