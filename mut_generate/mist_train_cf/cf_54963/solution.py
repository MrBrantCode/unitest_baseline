"""
QUESTION:
Write a function called `manipulate_string` that takes in a string `s` and performs the following operations in sequence: converts the string to lowercase, replaces all occurrences of a given substring `old` with a new substring `new`, and then splits the string into a list of words. The function should return the length of the resulting list of words. The function must be able to handle cases where `old` is not found in `s`.
"""

def manipulate_string(s, old, new):
    """
    This function takes in a string `s` and performs the following operations in sequence: 
    converts the string to lowercase, replaces all occurrences of a given substring `old` with a new substring `new`, 
    and then splits the string into a list of words. The function returns the length of the resulting list of words.

    Args:
        s (str): The input string.
        old (str): The substring to be replaced.
        new (str): The substring to replace with.

    Returns:
        int: The length of the resulting list of words.
    """
    s = s.lower()  # Convert the string to lowercase
    s = s.replace(old, new)  # Replace all occurrences of old with new
    return len(s.split())  # Split the string into a list of words and return the length