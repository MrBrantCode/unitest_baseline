"""
QUESTION:
Write a function `next_sequence_number` that generates the next number in the sequence where each term is obtained by multiplying the previous term by 2 and then adding 2. The function should take the last known term as input and return the next term in the sequence.
"""

def next_sequence_number(previous_number):
    """
    Generates the next number in the sequence where each term is obtained by multiplying the previous term by 2 and then adding 2.
    
    Args:
        previous_number (int): The last known term in the sequence.
    
    Returns:
        int: The next term in the sequence.
    """
    return previous_number * 2 + 2