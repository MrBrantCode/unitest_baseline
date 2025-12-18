"""
QUESTION:
Write a function `find_middle_positions` that finds the positions of all uppercase letters in a given string, excluding the first and last occurrences of each letter. The function should return a dictionary where the keys are the uppercase letters and the values are lists of their middle positions in the string.
"""

def find_middle_positions(s):
    """
    Finds the positions of all uppercase letters in a given string, 
    excluding the first and last occurrences of each letter.

    Args:
        s (str): The input string.

    Returns:
        dict: A dictionary where the keys are the uppercase letters 
              and the values are lists of their middle positions in the string.
    """
    uppercase_positions = {}
    for char in set(s.upper()):
        if char.isupper():
            positions = [i for i, x in enumerate(s) if x.upper() == char]
            if len(positions) > 2:
                uppercase_positions[char] = positions[1:-1]
    return uppercase_positions