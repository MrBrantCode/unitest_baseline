"""
QUESTION:
Create a function that will return true if all numbers in the sequence follow the same counting pattern. If the sequence of numbers does not follow the same pattern, the function should return false.

Sequences will be presented in an array of varied length. Each array will have a minimum of 3 numbers in it.

The sequences are all simple and will not step up in varying increments such as a Fibonacci sequence.

JavaScript examples:
"""

def is_arithmetic_sequence(seq):
    """
    Checks if the given sequence of numbers follows an arithmetic pattern.

    Parameters:
    seq (list of int): The sequence of numbers to be checked.

    Returns:
    bool: True if the sequence follows an arithmetic pattern, otherwise False.
    """
    return len({a - b for (a, b) in zip(seq, seq[1:])}) == 1