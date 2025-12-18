"""
QUESTION:
Implement a function `find_minimum(arr)` to find the minimum value in an unsorted array of integers. The function should not use any built-in sorting functions or data structures. The input array may be empty, in which case the function should return `None`. The function must have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the array.
"""

def find_minimum(arr):
    if len(arr) == 0:
        return None
    
    minimum = arr[0]
    for num in arr:
        if num < minimum:
            minimum = num
    
    return minimum