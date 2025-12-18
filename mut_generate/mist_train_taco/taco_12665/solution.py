"""
QUESTION:
Define a function that removes duplicates from an array of numbers and returns it as a result.

The order of the sequence has to stay the same.
"""

def remove_duplicates(seq):
    """
    Removes duplicates from an array of numbers while maintaining the original order.

    Parameters:
    seq (list of int): The input list of numbers.

    Returns:
    list of int: A list of numbers with duplicates removed, preserving the original order.
    """
    seen = set()
    result = []
    for num in seq:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result