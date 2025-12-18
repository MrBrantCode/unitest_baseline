"""
QUESTION:
Write a function `reverse_range(arr, start_index, end_index)` that takes an array of integers and a specified index range as input, reverses the elements within the specified index range in-place, and returns the modified array. The function should not create additional data structures for the reversed elements.
"""

def reverse_range(arr, start_index, end_index):
    """
    Reverses the elements within the specified index range in-place and returns the modified array.

    Args:
    arr (list): The input array of integers.
    start_index (int): The starting index of the range to be reversed (inclusive).
    end_index (int): The ending index of the range to be reversed (inclusive).

    Returns:
    list: The modified array with the elements within the specified index range reversed.
    """
    while start_index < end_index:
        arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
        start_index += 1
        end_index -= 1

    return arr