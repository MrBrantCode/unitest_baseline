"""
QUESTION:
Create a function `sort_by_frequency` that takes an array of integers as input and returns a new array with the integers sorted in descending order of their frequency of occurrence.
"""

def sort_by_frequency(arr):
    """
    Sorts an array of integers in descending order of their frequency of occurrence.

    Args:
    arr (list): A list of integers.

    Returns:
    list: A new list with the integers sorted in descending order of their frequency of occurrence.
    """
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else: 
            freq[i] = 1

    # Sort the list of tuples in descending order
    sorted_arr = sorted(freq.items(), key = lambda x : x[1], reverse = True)

    # Create list from sorted tuple
    return [i[0] for i in sorted_arr]