"""
QUESTION:
Implement a function named `bubble_sort` that takes an array of integers as input and returns the array sorted in descending order. The function should have a time complexity of O(n^2) and should not use any built-in sorting functions or libraries. The function should be able to handle arrays of up to 1 million elements.
"""

def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr