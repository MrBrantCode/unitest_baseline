"""
QUESTION:
Create a function called bubble_sort that implements the bubble sort algorithm to sort an array of positive and negative integers from smallest to largest while preserving the relative order of duplicate elements. The function should have a time complexity of O(n^2) and a space complexity of O(1). The input array can contain up to 1 million elements.
"""

def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr