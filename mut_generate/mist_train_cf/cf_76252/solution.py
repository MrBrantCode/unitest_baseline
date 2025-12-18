"""
QUESTION:
Write a function `char_frequency(s)` that takes a string `s` as input and returns a tuple containing the total character count and a dictionary with each character's frequency. The function should be case-sensitive and count spaces, punctuation, and special characters. If two characters have the same frequency, they should be listed in the order they appear in the string. Ensure that the input is of string type and handle cases where it might not be.
"""

def char_frequency(s):
    # Check if s is of string type
    if not isinstance(s, str):
        return "Error: Input must be a string"

    # Initialize an empty dictionary to store character frequencies
    freq_dict = {}

    # Traverse the string
    for char in s:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1

    # Return number of characters and individual frequencies
    return len(s), freq_dict