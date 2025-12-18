"""
QUESTION:
Given a sequence of integers, write a function `most_recurrent_digit` that returns the singular numerical digit with the highest recurrence. The function should take a list of integers as input and return the most recurrent digit. The input list will contain only positive integers.
"""

from collections import Counter

def most_recurrent_digit(sequence):
    """
    This function finds the most recurrent digit in a given sequence of integers.
    
    Args:
        sequence (list): A list of integers.
    
    Returns:
        int: The most recurrent singular digit in the sequence.
    """
    digit_counts = Counter(int(digit) for num in sequence for digit in str(num))
    return digit_counts.most_common(1)[0][0]