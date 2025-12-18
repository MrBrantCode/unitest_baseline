"""
QUESTION:
Write a function named `sort_array` that takes an array of integers as input and sorts it in increasing order, preserving the order of duplicate elements. The input array will have between 10 and 200 elements, and each element will be within the range of -10000 to 10000. The function should return the sorted array.
"""

def sort_array(arr):
    n = len(arr)
    
    # Iterate through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr