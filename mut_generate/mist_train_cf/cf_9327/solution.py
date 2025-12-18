"""
QUESTION:
Implement a function named `sort_with_duplicates` that sorts an array of integers in ascending order while handling duplicate elements efficiently. The function should return a new sorted array. The input array can contain any integer values, including negative numbers and zeros. The function's time complexity should be linear with respect to the size of the input array and the number of unique elements, and its space complexity should be linear as well.
"""

def sort_with_duplicates(arr):
    """
    Sorts an array of integers in ascending order while handling duplicate elements efficiently.

    Args:
        arr (list): A list of integers.

    Returns:
        list: A new sorted list of integers.
    """
    count_dict = {}
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    sorted_array = []
    for num in sorted(count_dict.keys()):
        sorted_array.extend([num] * count_dict[num])
    return sorted_array