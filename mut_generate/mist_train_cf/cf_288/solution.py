"""
QUESTION:
Create a function called `count_chars_reverse` that takes a string `s` and a character `c` as input. The function should remove all occurrences of `c` from `s` and return a dictionary where the keys are the remaining characters in `s` (in the order they appear when iterating over `s` in reverse order) and the values are their corresponding counts.
"""

def count_chars_reverse(s, c):
    """
    Removes all occurrences of a character c from a string s and returns a dictionary 
    where the keys are the remaining characters in s (in the order they appear when 
    iterating over s in reverse order) and the values are their corresponding counts.

    Args:
    s (str): The input string.
    c (str): The character to be removed.

    Returns:
    dict: A dictionary where keys are characters and values are their counts.
    """
    # Remove all occurrences of c from the original string
    s = s.replace(c, '')

    # Create a dictionary to store the counts of each character
    char_counts = {}

    # Iterate over characters in reverse order
    for char in reversed(s):
        # Check if the character is already in the dictionary
        if char in char_counts:
            # Increment the count of the character
            char_counts[char] += 1
        else:
            # Add the character to the dictionary with a count of 1
            char_counts[char] = 1

    # Return the dictionary
    return char_counts