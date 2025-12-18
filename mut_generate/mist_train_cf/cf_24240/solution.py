"""
QUESTION:
Write a function `predict_next_number` that takes a list of numbers as input and returns the next number in the sequence. The input sequence is expected to be a sequence of square numbers (i.e., numbers that can be expressed as n^2 for some integer n).
"""

def predict_next_number(sequence):
    """
    This function takes a list of square numbers as input and returns the next number in the sequence.
    
    Args:
        sequence (list): A list of square numbers.
    
    Returns:
        int: The next number in the sequence.
    """
    if not sequence:
        return None  # or raise an exception
    
    # Calculate the next number in the sequence
    next_number = (len(sequence) + 1) ** 2
    
    return next_number