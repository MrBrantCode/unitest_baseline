"""
QUESTION:
Implement the `insertion_sort` function to sort a list of strings in descending order based on the length of each string. If two strings have the same length, sort them in lexicographical order. The function should not modify the input list signature, and it can assume that the input list will only contain strings.
"""

def insertion_sort(arr):
    """
    Sorts a list of strings in descending order based on the length of each string.
    If two strings have the same length, sort them in lexicographical order.

    Args:
        arr (list): The list of strings to be sorted.

    Returns:
        list: The sorted list of strings.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and (len(arr[j]) < len(key) or (len(arr[j]) == len(key) and arr[j] < key)):
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
        
    return arr