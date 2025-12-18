"""
QUESTION:
Write a function `remove_duplicates_and_sort` that takes a string as input, removes all duplicate characters, and returns the remaining characters in a string sorted in ascending order based on their ASCII values. If there are no remaining characters after removing duplicates, return an empty string. The input string may contain both uppercase and lowercase letters, spaces, and special characters.
"""

def remove_duplicates_and_sort(s):
    """
    Removes duplicate characters from the input string and returns the remaining characters in a string 
    sorted in ascending order based on their ASCII values.

    Args:
        s (str): The input string.

    Returns:
        str: A string containing the unique characters from the input string, sorted in ascending order.
    """

    # Initialize an empty set to keep track of unique characters in the string
    unique_chars = set()

    # Iterate through each character in the string
    for c in s:
        # If the character is not in unique_chars, add it to unique_chars
        if c not in unique_chars:
            unique_chars.add(c)

    # Convert unique_chars to a list and sort it in ascending order based on the ASCII values of the characters
    sorted_chars = sorted(list(unique_chars))

    # Join the sorted list into a string and return it
    return ''.join(sorted_chars)