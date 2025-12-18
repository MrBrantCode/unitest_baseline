"""
QUESTION:
Implement the function `bubble_sort` that takes an array of integers as input, sorts it in ascending order using the Bubble Sort algorithm with a time complexity of O(n^2), and returns the sorted array. The implementation should only use array manipulation and comparison operators.
"""

def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n-1):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr