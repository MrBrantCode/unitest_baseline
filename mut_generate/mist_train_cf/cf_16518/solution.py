"""
QUESTION:
Create a function `longest_string` that takes two strings `str1` and `str2` as arguments. The function should return the longest string with any duplicate characters removed. Implement the logic to remove duplicate characters without using any built-in functions or libraries that can directly remove duplicate characters.
"""

def longest_string(str1, str2):
    """
    Returns the longest string with any duplicate characters removed.

    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.

    Returns:
        str: The longest string with duplicates removed.
    """
    # Determine the longest string
    longest = str1 if len(str1) > len(str2) else str2

    # Initialize an empty string to store the result
    result = ""

    # Iterate over each character in the longest string
    for char in longest:
        # Add the character to the result if it is not already present
        if char not in result:
            result += char

    return result