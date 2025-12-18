"""
QUESTION:
Write a function `sum_of_array` that calculates the sum of all integer values in a given two-dimensional array. The function should take a 2D array `arr` as input and return the sum of its elements. The array has dimensions `m`x`n`, where `m` and `n` are up to 10^6, and each element is in the range -100 to 100, inclusive. The function should have a time complexity of O(mn) and a memory space complexity of O(1).
"""

def sum_of_array(arr):
    m = len(arr)
    n = len(arr[0])
    
    total_sum = 0
    
    for i in range(m):
        for j in range(n):
            total_sum += arr[i][j]
    
    return total_sum