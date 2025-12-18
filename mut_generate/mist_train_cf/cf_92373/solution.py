"""
QUESTION:
Implement the function `remove_duplicates` that takes a string as input and returns the string with all consecutive duplicates removed. The function should modify the string in-place, without using any additional space that scales with input size.
"""

def remove_duplicates(s):
    if not s:
        return s

    # Convert string to a list of characters
    chars = list(s)
    n = len(chars)

    # Initialize the pointer to keep track of the last non-duplicate character
    last_non_duplicate = 0

    # Iterate through the characters
    for i in range(1, n):
        # If the current character is different from the last non-duplicate character
        if chars[i] != chars[last_non_duplicate]:
            last_non_duplicate += 1
            # Move the current character to its correct position
            chars[last_non_duplicate] = chars[i]

    # Convert the remaining characters back to a string and return it
    return ''.join(chars[:last_non_duplicate + 1])