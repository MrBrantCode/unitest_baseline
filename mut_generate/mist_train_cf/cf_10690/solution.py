"""
QUESTION:
Create a function called `sort_by_frequency_desc` that takes a list of integers as input and returns the sorted list. The sorting should be done based on the frequency of occurrence of each integer in descending order. If multiple integers have the same frequency, they should be sorted in descending order of their values.
"""

def sort_by_frequency_desc(arr):
    """
    Sorts the input list based on the frequency of occurrence of each integer in descending order.
    If multiple integers have the same frequency, they are sorted in descending order of their values.

    Args:
        arr (list): The input list of integers.

    Returns:
        list: The sorted list.
    """
    freq_dict = {}
    for num in arr:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1

    return sorted(arr, key=lambda x: (freq_dict[x], -x), reverse=True)