"""
QUESTION:
Implement a function called `insertion_sort` that sorts an array of elements in ascending order using the insertion sort algorithm. The function should take a list of elements as input and return a new sorted list.
"""

def insertion_sort(arr):
    """
    Sorts an array of elements in ascending order using the insertion sort algorithm.

    Args:
        arr (list): A list of elements to be sorted.

    Returns:
        list: A new sorted list.
    """
    # Create a copy of the input array to avoid modifying it in-place
    arr_copy = arr.copy()

    # Iterate over the array starting from the second element
    for i in range(1, len(arr_copy)):
        key = arr_copy[i]
        j = i - 1

        # Compare the current element with the elements in the sorted region
        while j >= 0 and arr_copy[j] > key:
            # Shift the elements if necessary
            arr_copy[j + 1] = arr_copy[j]
            j -= 1

        # Insert the current element at the correct position
        arr_copy[j + 1] = key

    return arr_copy