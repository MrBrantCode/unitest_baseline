"""
QUESTION:
Implement a function called `modified_insertion_sort(arr)` that sorts an array of integers in descending order. The function should take an array of integers as input and return the sorted array in descending order.
"""

def modified_insertion_sort(arr):
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr