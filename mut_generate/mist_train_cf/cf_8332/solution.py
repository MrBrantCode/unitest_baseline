"""
QUESTION:
Write a function called `bubble_sort` that takes in an array of integers and returns the sorted array in decreasing order using the bubble sort algorithm. Implement the bubble sort algorithm from scratch and do not use any built-in sorting functions or libraries. Handle cases where the array is empty or has only one element.
"""

def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap if the current element is less than the next element
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr