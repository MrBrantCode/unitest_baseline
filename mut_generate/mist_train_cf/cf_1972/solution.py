"""
QUESTION:
Create a function named `bubble_sort` that sorts an array of positive and negative integers in ascending order while preserving the relative order of duplicate elements. The function should use the bubble sort algorithm with a time complexity of O(n^2) and a space complexity of O(1), where n is the number of elements in the array. The input array can contain up to 1 million integers.
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