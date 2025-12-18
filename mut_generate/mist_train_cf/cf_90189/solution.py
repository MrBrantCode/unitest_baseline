"""
QUESTION:
Implement the bubble sort algorithm in a function called `bubble_sort` that takes an array of integers as input and returns the sorted array in ascending order. The function should have a time complexity of O(n^2) and a space complexity of O(1), where n is the length of the array.
"""

def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr