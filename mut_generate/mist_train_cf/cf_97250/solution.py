"""
QUESTION:
Implement a function called `bubble_sort` that takes in an array of integers and returns the sorted array in decreasing order using the bubble sort algorithm. The function should compare each pair of adjacent elements, swap them if they are in the wrong order, and continue this process until the entire array is sorted. The function should handle cases where the array is empty or has only one element.
"""

def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            
            # Traverse the array from 0 to n-i-1 and swap if the element found is greater
            # than the next element
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr