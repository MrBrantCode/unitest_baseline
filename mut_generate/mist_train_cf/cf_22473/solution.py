"""
QUESTION:
Implement a function `bubble_sort(arr)` that takes an array of integers as input and returns the array in ascending order using the bubble sort algorithm. The function must have a time complexity of O(n^2) and a space complexity of O(1), where n is the length of the array.
"""

def entance(arr):
    n = len(arr)
    
    # Traverse through all elements in the array
    for i in range(n):
        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr