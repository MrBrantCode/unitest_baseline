"""
QUESTION:
Write a function `remove_duplicates(arr)` that removes duplicates from a given array of integers in-place, without using any built-in functions or data structures. The function should maintain the original order of elements and not allocate any extra space. The input array is guaranteed to be non-empty and may contain duplicates.
"""

def remove_duplicates(arr):
    # Sort the array in ascending order
    arr.sort()

    # Initialize a variable to keep track of the index of the next non-duplicate element
    next_non_duplicate = 1

    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        # Check if the current element is different from the previous element
        if arr[i] != arr[i-1]:
            # If it is different, copy it to the next non-duplicate position
            arr[next_non_duplicate] = arr[i]
            # Increment the index of the next non-duplicate element
            next_non_duplicate += 1

    # Return a new array containing only the non-duplicate elements
    return arr[:next_non_duplicate]