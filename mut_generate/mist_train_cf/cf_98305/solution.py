"""
QUESTION:
Create a function called `bubble_sort` that sorts a list of integers in ascending order using the bubble sort algorithm. The function should take a list of integers as input and return the sorted list. The function should have a time complexity of O(n^2).
"""

def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr