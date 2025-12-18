"""
QUESTION:
Generate a sequence of integers from 0 to a given integer 'n' as a list. The function should take an integer 'n' as input and return a list of integers from 0 to 'n' (inclusive). Implement this using the function name 'generate_sequence'.
"""

def generate_sequence(n):
    """
    Generate a sequence of integers from 0 to a given integer 'n' as a list.
    
    Args:
        n (int): The upper limit of the sequence.
    
    Returns:
        list: A list of integers from 0 to 'n' (inclusive).
    """
    return list(range(n + 1))