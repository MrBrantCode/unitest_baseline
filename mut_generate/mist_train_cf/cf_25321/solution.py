"""
QUESTION:
Implement a function called `sort` that takes an array of elements as input and returns the sorted array in ascending order. The function should use a selection sort algorithm, which sorts an array by repeatedly finding the minimum element from the unsorted part and swapping it with the first unsorted element.
"""

def sort(arr):
    n = len(arr)
    
    # Various loops to sort the array 
    for i in range(n): 
        min_idx = i 
        for j in range(i+1, n): 
            if arr[min_idx] > arr[j]: 
                min_idx = j 
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 
    return arr