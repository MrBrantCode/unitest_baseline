"""
QUESTION:
Write a function called "string_length" that takes a string as input, removes any leading or trailing whitespaces, and returns the number of characters in the string. The function should not use built-in functions like len() and should be able to handle strings with multiple lines, special characters, and Unicode characters, with a maximum length of 10^6 characters.
"""

def string_length(s):
    """
    This function takes a string as input, removes any leading or trailing whitespaces, 
    and returns the number of characters in the string.

    Args:
        s (str): The input string.

    Returns:
        int: The number of characters in the string.
    """

    # Remove any leading or trailing whitespaces from the string
    s = s.strip()

    # Initialize a variable, `count`, to 0
    count = 0

    # Iterate over each character, `c`, in the string
    for c in s:
        # If `c` is not a whitespace, increment `count` by 1
        if c != ' ':
            count += 1

    # Return the value of `count`
    return count