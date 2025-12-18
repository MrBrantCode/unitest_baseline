"""
QUESTION:
Implement the `quicksort` function that recursively sorts a list of integers using the quicksort algorithm with a time complexity of O(n log n) and a space complexity of O(log n). The function should handle duplicate elements and should not use any built-in sorting functions or libraries.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    
    return quicksort(less) + equal + quicksort(greater)