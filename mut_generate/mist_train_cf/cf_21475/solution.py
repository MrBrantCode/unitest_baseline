"""
QUESTION:
Implement a function `is_strictly_increasing` that checks if a given sequence is a strictly increasing arithmetic sequence with a common difference of 1. The function should take a sequence as input and return a boolean value indicating whether the sequence meets the specified condition. The function must have a time complexity of O(n) and a space complexity of O(1), where n is the length of the sequence.
"""

def is_strictly_increasing(sequence):
    """
    Checks if a given sequence is a strictly increasing arithmetic sequence with a common difference of 1.

    Args:
        sequence (list): The input sequence to be checked.

    Returns:
        bool: True if the sequence is a strictly increasing arithmetic sequence with a common difference of 1, False otherwise.
    """
    if len(sequence) < 2:
        return False
    previous = sequence[0]
    for current in sequence[1:]:
        if current != previous + 1:
            return False
        previous = current
    return True