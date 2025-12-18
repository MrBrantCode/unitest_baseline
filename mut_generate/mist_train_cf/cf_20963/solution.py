"""
QUESTION:
Implement the `insertion_sort` function to sort a list of positive integers in ascending order. The list can contain duplicates and its length is up to 100,000. The function should take the list as input, sort it in-place, and return the sorted list.
"""

def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i-1
        
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key
    
    return arr