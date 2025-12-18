"""
QUESTION:
Implement a stable sorting function, `bubble_sort`, that takes a list of integers as input and returns the sorted list in ascending order. The function should have a time complexity of O(n^2) or less and preserve the relative order of equal elements.
"""

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Flag to check if any swap occurred in the current iteration
        swapped = False
        
        for j in range(n-i-1):
            # Check if the current element is greater than the next element
            if arr[j] > arr[j+1]:
                # Swap the elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # If no swap occurred in the current iteration, the list is already sorted
        if not swapped:
            break
    
    return arr