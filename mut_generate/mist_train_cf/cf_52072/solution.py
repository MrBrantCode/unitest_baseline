"""
QUESTION:
Create a function called `find_sequence(T, q)` that takes two parameters: a string `T` representing the text data, and a string `q` representing the sequence to be found. The function should return a tuple containing the position of the first appearance of `q` in `T` and the total count of `q` in `T`. The position should be 0-indexed, and if `q` is not found in `T`, the position should be -1. The function should work for any valid string inputs `T` and `q`.
"""

def find_sequence(T, q):
    """
    This function finds the position of the first appearance of a sequence q in a text T and returns the total count of q in T.

    Args:
        T (str): The text data.
        q (str): The sequence to be found.

    Returns:
        tuple: A tuple containing the position of the first appearance of q in T and the total count of q in T.
    """
    position = T.find(q)
    count = T.count(q)
    return position, count