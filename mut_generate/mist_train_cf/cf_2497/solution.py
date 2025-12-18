"""
QUESTION:
Implement a function `find_second_min(arr)` to find the second minimum value in an unsorted array of integers without using any built-in sorting functions or data structures. The function should iterate through the array only once, resulting in a time complexity of O(n). However, in this case, the time complexity has to be O(n log n), but that is not possible to be achieved with a single loop. Therefore we need to accept the fact that this function is not possible in O(n log n) with the given conditions, but we can do it in O(n) time complexity.
"""

def find_second_min(arr):
    min1 = float('inf')
    min2 = float('inf')
    
    for num in arr:
        if num < min1:
            min2 = min1
            min1 = num
        elif num > min1 and num < min2:
            min2 = num
    
    return min2