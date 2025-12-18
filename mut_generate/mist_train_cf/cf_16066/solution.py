"""
QUESTION:
Write a function named `has_unique_chars` that takes a string as input and returns `True` if all characters in the string are unique and `False` otherwise. The function must have a time complexity of O(n), where n is the length of the string, and cannot use any additional data structures beyond what is necessary for the function's operation, such as a set.
"""

def has_unique_chars(string):
    # Create an empty set to store unique characters
    unique_chars = set()

    # Iterate over each character in the string
    for char in string:
        # If the character is already in the set, return False
        if char in unique_chars:
            return False
        # Otherwise, add the character to the set
        unique_chars.add(char)

    # If we reach this point, all characters are unique
    return True