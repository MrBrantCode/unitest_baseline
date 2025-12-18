"""
QUESTION:
Create a function `arithmetic_sequence` that takes a list of numbers as input and returns the formula for generating the arithmetic sequence if the input list represents an arithmetic sequence. If the input list does not represent an arithmetic sequence or has less than two numbers, the function should return an error message.
"""

def arithmetic_sequence(sequence):
    """
    This function takes a list of numbers as input and returns the formula for generating 
    the arithmetic sequence if the input list represents an arithmetic sequence. 
    If the input list does not represent an arithmetic sequence or has less than two numbers, 
    the function returns an error message.

    Args:
        sequence (list): A list of numbers.

    Returns:
        str: The formula for the arithmetic sequence, or an error message.
    """
    n = len(sequence)
    if n < 2:
        return "Sequence must have at least two numbers."
    d = sequence[1] - sequence[0]
    for i in range(2, n):
        if sequence[i] - sequence[i-1] != d:
            return "Sequence is not arithmetic."
    a = sequence[0]
    return f"The formula for this arithmetic sequence is: {a} + {d}n"