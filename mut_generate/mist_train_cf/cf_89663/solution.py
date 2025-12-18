"""
QUESTION:
Implement a recursive quicksort function in Python with a time complexity of O(n log n) and a space complexity of O(log n). The function should take a list of integers as input and return a sorted list of integers. The list can contain duplicate elements and the function should not use any built-in sorting functions or libraries.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    
    return quicksort(less) + equal + quicksort(greater)