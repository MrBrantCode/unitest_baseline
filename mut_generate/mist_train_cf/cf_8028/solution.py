"""
QUESTION:
Implement the `insertion_sort_desc` function, which sorts an array of integers in descending order using the insertion sort algorithm. The function should have a time complexity of O(n^2) and should not use any built-in sorting functions or libraries. The array can contain duplicate elements.
"""

def insertion_sort_desc(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and arr[j] < key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr