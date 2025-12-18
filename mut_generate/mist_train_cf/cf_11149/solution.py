"""
QUESTION:
Implement the `bubble_sort` function to sort a given list in increasing order using the bubble sort algorithm. The function should not use any built-in sorting functions or libraries. It should handle edge cases such as an empty list, a list with only one element, or a list with duplicate elements. The function should optimize for efficiency, considering time complexity and space complexity.
"""

def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1. Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr