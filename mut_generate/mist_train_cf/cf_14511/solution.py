"""
QUESTION:
Write a function called `insert_element` that inserts a specific integer element at the beginning of a fixed-length array of 10 integers, shifting all other elements to the right. If the array is already full, remove the oldest element before inserting the new element. The array and element should only store integers between 1 and 100 (inclusive).
"""

def insert_element(arr, element):
    """
    Inserts a specific integer element at the beginning of a fixed-length array of 10 integers,
    shifting all other elements to the right. If the array is already full, remove the oldest 
    element before inserting the new element.

    Args:
        arr (list): A list of integers with a maximum length of 10.
        element (int): An integer between 1 and 100 (inclusive) to be inserted.

    Returns:
        list: The modified array with the new element inserted.
    """
    if len(arr) < 10:
        arr.insert(0, element)
    else:
        arr.pop()
        arr.insert(0, element)
    return arr