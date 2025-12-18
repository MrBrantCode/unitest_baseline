"""
QUESTION:
Write a function `find_float` that takes a sequence as input and returns a list of tuples. Each tuple should contain the index and value of a floating point number in the sequence. The function should be able to handle sequences that contain various data types and structures.
"""

def find_float(seq):
    """
    Returns a list of tuples containing the index and value of floating point numbers in the sequence.
    
    Args:
        seq (sequence): A sequence containing various data types and structures.
    
    Returns:
        list: A list of tuples, where each tuple contains the index and value of a float in the sequence.
    """
    return [(i, val) for i, val in enumerate(seq) if isinstance(val, float)]