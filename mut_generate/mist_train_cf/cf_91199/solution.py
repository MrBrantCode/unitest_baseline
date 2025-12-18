"""
QUESTION:
Implement the `bubble_sort` function to sort an array of strings in alphabetical order without using any built-in sorting functions or methods. The function should take an array of strings as input and return the sorted array.
"""

def entance(arr):
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