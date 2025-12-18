"""
QUESTION:
Implement a function `quicksort(arr)` that sorts an array of distinct integers in ascending order without using any built-in sorting functions or libraries. The function should have a time complexity of O(n log n) and use constant space complexity.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    smaller = []
    larger = []
    
    for i in range(len(arr) - 1):
        if arr[i] <= pivot:
            smaller.append(arr[i])
        else:
            larger.append(arr[i])
    
    return quicksort(smaller) + [pivot] + quicksort(larger)