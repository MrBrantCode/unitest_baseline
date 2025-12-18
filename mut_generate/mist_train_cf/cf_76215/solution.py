"""
QUESTION:
Find the missing number in a sequence where each number is twice the previous one. Write a function `find_missing_number` that takes a list of numbers as input and returns the missing number in the sequence. The input list will contain at least two numbers, and the missing number will be the next number in the sequence.
"""

def find_missing_number(numbers):
    """
    Find the missing number in a sequence where each number is twice the previous one.

    Args:
        numbers (list): A list of numbers in the sequence.

    Returns:
        int: The missing number in the sequence.
    """
    # Find the missing number by multiplying the last number by 2
    return numbers[-1] * 2