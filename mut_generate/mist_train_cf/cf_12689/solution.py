"""
QUESTION:
Write a function `common_characters` that takes two strings as input and returns the number of common characters between the two strings. You can only use basic string manipulation operations such as indexing and concatenation, and you are not allowed to use any built-in string methods or data structures such as lists or dictionaries.
"""

def common_characters(string_1, string_2):
    """
    Returns the number of common characters between two strings.
    
    Args:
    string_1 (str): The first input string.
    string_2 (str): The second input string.
    
    Returns:
    int: The number of common characters.
    """
    common_chars = 0

    # Loop through each character in string_1
    for char in string_1:
        # Check if the character is also present in string_2
        if char in string_2:
            common_chars += 1

    return common_chars