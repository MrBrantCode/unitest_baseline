"""
QUESTION:
Implement the function insertElement(arr, newElement) to insert a new element into an existing unsorted array with the most efficient time complexity. The function should take an array (arr) and the new element to be inserted (newElement) as parameters and return the updated array.
"""

def insertElement(arr, newElement):
    """
    Inserts a new element into an existing unsorted array.

    Args:
        arr (list): The existing array.
        newElement: The new element to be inserted.

    Returns:
        list: The updated array with the new element.
    """
    arr.append(newElement)
    return arr