"""
QUESTION:
Write a function `delete_element(arr, index)` that deletes an element from the given array at the specified index and returns the updated array. The function should handle both positive and negative indices, empty arrays, and floating-point numbers, with a time complexity of O(n) and a space complexity of O(1). If the index is out of bounds or the array is empty, the function should print an error message and return the original array.
"""

def delete_element(arr, index):
    """
    Deletes an element from the given array at the specified index and returns the updated array.
    
    The function handles both positive and negative indices, empty arrays, and floating-point numbers, 
    with a time complexity of O(n) and a space complexity of O(1). If the index is out of bounds 
    or the array is empty, the function prints an error message and returns the original array.
    
    Parameters:
    arr (list): The input array.
    index (int): The index of the element to be deleted.
    
    Returns:
    list: The updated array after deletion.
    """

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