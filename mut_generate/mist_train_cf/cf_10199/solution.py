"""
QUESTION:
Write a function `delete_even_numbers` that takes an array of integers as input, deletes all even numbers from the array in-place, and returns the modified array. The function should iterate backwards from the last index to the first index. You are not allowed to use any built-in array manipulation functions or create a new array to store the result.
"""

def delete_even_numbers(arr):
    """
    Deletes all even numbers from the given array in-place, 
    iterating backwards from the last index to the first index.

    Args:
        arr (list): The input array of integers.

    Returns:
        list: The modified array with all even numbers removed.
    """
    i = len(arr) - 1
    while i >= 0:
        if arr[i] % 2 == 0:
            # Delete even number from array by shifting remaining elements to the left
            for j in range(i, len(arr) - 1):
                arr[j] = arr[j + 1]
            # Reduce the length of the array by 1
            arr.pop()
        i -= 1
    return arr