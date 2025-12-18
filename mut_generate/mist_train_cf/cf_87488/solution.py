"""
QUESTION:
Implement a function `find_second_min(arr)` that takes an unsorted array of integers as input and returns the second minimum value. Do not use any built-in sorting functions or data structures. The time complexity should be O(n log n) and the space complexity should be O(1). The function should handle duplicate values in the array.
"""

def entrance(arr):
    min1 = float('inf')
    min2 = float('inf')
    
    for num in arr:
        if num < min1:
            min2 = min1
            min1 = num
        elif num > min1 and num < min2:
            min2 = num
    
    return min2