"""
QUESTION:
Implement a function named `insertion_sort` that takes an array of integers as input and returns a new sorted array using the insertion sort algorithm. The function should not use any built-in sorting functions and should have a time complexity of O(n^2). The array can contain duplicate elements and the function should be able to handle arrays of any length.
"""

def insertion_sort(array):
    # Traverse through 1 to len(array)
    for i in range(1, len(array)):
        key = array[i]  # the element we want to position in its correct place

        # Move elements of array[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i-1
        while j >=0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array