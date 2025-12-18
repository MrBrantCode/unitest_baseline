"""
QUESTION:
Write a function `concat_strings` that takes two strings as input, `str1` and `str2`. The function should return a string that is the concatenation of `str1` and `str2`, with all characters in uppercase, containing only alphabetical characters, and sorted in reverse alphabetical order. `str1` should not exceed 10 characters, and `str2` should be at least 5 characters long. The resulting string should also not contain any duplicate characters.
"""

def concat_strings(str1, str2):
    """
    Concatenates two strings, ensuring uppercase, alphabetical characters, 
    maximum length, minimum length, sorted in reverse order, and no duplicates.

    Args:
    str1 (str): The first string.
    str2 (str): The second string.

    Returns:
    str: The concatenated string.
    """

    # Convert strings to uppercase
    str1 = str1.upper()
    str2 = str2.upper()

    # Remove non-alphabetical characters
    str1 = ''.join(filter(str.isalpha, str1))
    str2 = ''.join(filter(str.isalpha, str2))

    # Ensure length constraints
    str1 = str1[:10]  # truncate if too long
    str2 = str2.ljust(5, 'A')  # pad with 'A' if too short

    # Concatenate, remove duplicates, and sort in reverse order
    result = ''.join(sorted(set(str1 + str2), reverse=True))

    return result