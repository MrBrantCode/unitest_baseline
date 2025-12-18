"""
QUESTION:
Write a function named `reverse_string` that takes a string `s` as input and returns the reversed string without using any built-in string manipulation functions or data structures. The function should have a time complexity of O(n), where n is the length of the input string. The function should handle strings with whitespace characters, special characters, and consecutive whitespace characters as a single whitespace character in the reversed string.
"""

def reverse_string(s):
    # Convert the string to a list of characters
    # so that we can modify it in-place
    chars = list(s)

    # Initialize the pointers
    start = 0
    end = len(chars) - 1

    # Loop until the pointers meet in the middle
    while start < end:
        # If the start pointer is at a whitespace character,
        # move it to the next non-whitespace character
        if chars[start].isspace():
            while start < end and chars[start].isspace():
                start += 1

        # If the end pointer is at a whitespace character,
        # move it to the next non-whitespace character
        if chars[end].isspace():
            while start < end and chars[end].isspace():
                end -= 1

        # Swap the characters at the start and end pointers
        chars[start], chars[end] = chars[end], chars[start]

        # Move the pointers towards each other
        start += 1
        end -= 1

    # Convert the list of characters back to a string
    return ''.join(chars)