"""
QUESTION:
Write a function `reverse_array` that takes an array as an input, reverses its elements in-place without using any loops or built-in array manipulation functions, and returns the modified array. The function must have a time complexity of O(1) and cannot create a new array to store the reversed elements. The function should be able to handle arrays of up to 10^5 elements.
"""

def reverse_array(arr):
    """
    Reverses an array in-place without using any loops or built-in array manipulation functions.

    Args:
        arr (list): The array to be reversed.

    Returns:
        list: The modified array.
    """
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def _reverse_array(i):
        if i < len(arr) // 2:
            swap(i, len(arr) - i - 1)
            _reverse_array(i + 1)

    _reverse_array(0)
    return arr