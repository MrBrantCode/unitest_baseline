"""
QUESTION:
Write a function `transform_to_float_list` that takes a string of space-separated numbers as input and returns a list of floating-point numbers.
"""

def transform_to_float_list(char_sequence):
    """
    This function takes a string of space-separated numbers as input, 
    and returns a list of floating-point numbers.
    
    Args:
    char_sequence (str): A string of space-separated numbers.
    
    Returns:
    list: A list of floating-point numbers.
    """
    return [float(num_str) for num_str in char_sequence.split()]