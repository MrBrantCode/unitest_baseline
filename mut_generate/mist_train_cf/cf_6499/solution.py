"""
QUESTION:
Implement a function `count_unique_characters` that takes an input string `s` and returns the number of unique alphanumeric characters it contains, ignoring punctuation marks, special characters, and considering only alphanumeric characters in a case-insensitive manner. The function should not use any built-in functions for counting unique characters, have a time complexity of O(n), and a space complexity of O(k), where n is the length of the input string and k is the number of unique alphanumeric characters in the string.
"""

def count_unique_characters(s):
    # Create a set to store unique alphanumeric characters
    unique_chars = set()

    # Remove punctuation marks and special characters from the string
    s = ''.join(c for c in s if c.isalnum())

    # Convert the string to lowercase
    s = s.lower()

    # Iterate over each character in the string
    for char in s:
        # Add the character to the set if it is not already present
        unique_chars.add(char)

    # Return the number of unique characters
    return len(unique_chars)