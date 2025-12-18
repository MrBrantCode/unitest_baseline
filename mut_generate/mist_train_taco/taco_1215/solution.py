"""
QUESTION:
Your task is simply to count the total number of lowercase letters in a string.

## Examples
"""

def count_lowercase_letters(input_string: str) -> int:
    """
    Counts the total number of lowercase letters in the given input string.

    Parameters:
    input_string (str): The string to be analyzed.

    Returns:
    int: The total number of lowercase letters in the input string.
    """
    return sum(1 for char in input_string if char.islower())