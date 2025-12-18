"""
QUESTION:
Write a function called `count_occurrences` that takes two parameters: a list `arr` and an element. The function should return the number of occurrences of the given element in the list without using any built-in functions or libraries. The list may contain duplicate elements, negative integers, and floats, and may have a maximum length of 1000. The function should handle the case when the element to be searched is not present in the list, and should have a time complexity of O(n) and space complexity of O(1).
"""

def count_occurrences(arr, element):
    """
    Counts the occurrences of a given element in a list without using any built-in functions or libraries.

    Args:
        arr (list): The list to search in.
        element: The element to search for.

    Returns:
        int: The number of occurrences of the element in the list.
    """
    count = 0
    for i in range(len(arr)):
        if arr[i] == element:
            count += 1
    return count