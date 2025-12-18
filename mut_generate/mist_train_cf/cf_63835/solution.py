"""
QUESTION:
Create a function named `generate_sequence` that takes two parameters, `start` and `end`, representing the beginning and end of the sequence respectively. The function should return a string representing a series of numbers from `start` to `end` separated by a comma and a space. The function should not use regular expressions.
"""

def generate_sequence(start, end):
    """
    This function generates a string representing a series of numbers 
    from 'start' to 'end' separated by a comma and a space.

    Args:
        start (int): The beginning of the sequence.
        end (int): The end of the sequence.

    Returns:
        str: A string representing the sequence of numbers.
    """
    sequence = ", ".join(str(i) for i in range(start, end + 1))
    return sequence