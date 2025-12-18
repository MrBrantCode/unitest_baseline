"""
QUESTION:
Write a function `find_median(arr)` that takes a list of integers as input, sorts the list, and returns the median value. The function should handle the following cases: 

- If the list is empty, return `None`.
- If the list has an odd number of elements, return the middle value.
- If the list has an even number of elements, return the average of the two middle values.
- The function should also handle lists with duplicate values.
"""

def find_median(arr):
    if len(arr) == 0:
        return None
    
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    middle = n // 2
    
    if n % 2 == 1:  
        return sorted_arr[middle]
    else:  
        return (sorted_arr[middle-1] + sorted_arr[middle]) / 2