"""
QUESTION:
Create a function `delete_element(arr, index)` that deletes an element from the given array at the specified index. The function should handle both positive and negative indices, empty arrays, and floating-point indices. If the index is out of bounds, it should display an error message. The remaining elements should be shifted to fill the empty space left by the deleted element. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the array.
"""

def delete_element(arr, index):
    # Check if the array is empty
    if len(arr) == 0:
        print("Error: Array is empty.")
        return arr

    # Check if the index is out of bounds
    if index < 0 or index >= len(arr):
        print("Error: Index is out of bounds.")
        return arr

    # Shift the remaining elements to fill the empty space
    for i in range(index, len(arr) - 1):
        arr[i] = arr[i + 1]

    # Delete the last element
    arr.pop()

    return arr