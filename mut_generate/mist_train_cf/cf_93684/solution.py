"""
QUESTION:
Write a function `delete_element(arr, index)` that deletes an element from array `arr` at the specified `index`. Ensure the function handles both positive and negative indices, empty arrays, and floating-point indices. If the index is out of bounds or the array is empty, the function should print an error message and return the original array. Otherwise, the function should print the deleted element, shift the remaining elements to fill the gap, and return the updated array.
"""

def delete_element(arr, index):
    # Check if array is empty
    if len(arr) == 0:
        print("Error: Array is empty")
        return arr

    # Check if index is out of bounds
    if index < -len(arr) or index >= len(arr):
        print("Error: Index is out of bounds")
        return arr

    # Convert floating-point index to integer
    index = int(index)

    # Delete element at given index
    if index < 0:
        index += len(arr)  # Convert negative index to positive
    deleted_element = arr.pop(index)

    print("Deleted element:", deleted_element)
    return arr