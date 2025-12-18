"""
QUESTION:
Create a function named `search` that takes two parameters: an array and an element. The function should return a list of indices of all occurrences of the given element in the array. If the element is not found, return an empty list. The function should be able to handle arrays with duplicate elements.
"""

def search(array, element):
    """
    Returns a list of indices of all occurrences of the given element in the array.

    Args:
        array (list): The input array to search in.
        element: The element to search for.

    Returns:
        list: A list of indices of all occurrences of the given element.
    """
    occurrences = [i for i, x in enumerate(array) if x == element]
    return occurrences