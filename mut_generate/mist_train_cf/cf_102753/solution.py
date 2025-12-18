"""
QUESTION:
Implement a function `get_second_largest` to find the second largest element in a sequence. The function should take a list of numbers as input, handle sequences of any length, and return the second largest number. If the sequence has less than two distinct elements, the function should return `None`.
"""

def get_second_largest(seq):
    """
    Find the second largest element in a sequence.

    Args:
    seq (list): A list of numbers.

    Returns:
    The second largest number in the sequence, or None if the sequence has less than two distinct elements.
    """
    if len(seq) < 2:
        return None
    largest = float('-inf')
    second_largest = float('-inf')
    for num in seq:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest