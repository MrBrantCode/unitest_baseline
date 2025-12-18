"""
QUESTION:
Generate a function `generate_strings` that takes an integer `n` as input and returns all possible strings of length `n` using the characters 'A', 'B', and 'C'.
"""

def generate_strings(n):
    """
    Generate all possible strings of length n using the characters 'A', 'B', and 'C'.

    Args:
        n (int): The length of the strings to generate.

    Returns:
        list: A list of all possible strings of length n.
    """
    if n == 0:
        return ['']
    else:
        return [char + string for char in 'ABC' for string in generate_strings(n-1)]