"""
QUESTION:
Implement a function `bubble_sort` that takes a list of integers as input, sorts it in ascending order using the Bubble Sort algorithm, and returns the sorted list. The function should have a time complexity of O(n^2) and a space complexity of O(1), and it should handle lists containing both positive and negative integers, duplicate integers, empty lists, lists of length 1, and large input lists with thousands or millions of elements.
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