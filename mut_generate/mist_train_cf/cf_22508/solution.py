"""
QUESTION:
Implement the `insertion_sort_desc` function to sort an array of integers in descending order using the insertion sort algorithm. The array can contain duplicate elements and the algorithm should have a time complexity of O(n^2).
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