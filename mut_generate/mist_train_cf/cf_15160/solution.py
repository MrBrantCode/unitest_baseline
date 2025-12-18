"""
QUESTION:
Write a function `count_occurrences` that counts the number of occurrences of an element in a list without using built-in functions or libraries. The list can have a maximum length of 1000 and may contain duplicate elements, negative integers, and floats. The function should have a time complexity of O(n) and space complexity of O(1), and handle cases when the element to be searched is not present in the list.
"""

def count_occurrences(arr, element):
    """
    Counts the number of occurrences of an element in a list.

    Args:
        arr (list): The list to search in.
        element: The element to search for.

    Returns:
        int: The number of occurrences of the element.

    Time complexity: O(n)
    Space complexity: O(1)
    """
    count = 0
    for num in arr:
        if num == element:
            count += 1
    return count