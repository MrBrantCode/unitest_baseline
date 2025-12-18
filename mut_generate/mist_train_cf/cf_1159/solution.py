"""
QUESTION:
Write a function `sort_list_descending` that takes a list of integers as input and returns a new list with the integers sorted in descending order. The function should not use any built-in sorting functions or libraries.
"""

def sort_list_descending(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n - 1):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater
            # than the next element
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr