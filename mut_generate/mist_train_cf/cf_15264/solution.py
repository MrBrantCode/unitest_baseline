"""
QUESTION:
Write a function named `find_first_non_repeating_char` that takes a string `input_str` as input and returns the first non-repeating character in the string without using any built-in Python functions or libraries. The input string can contain special characters or numbers. If no non-repeating character is found, return `None`.
"""

def find_first_non_repeating_char(input_str):
    # Create a dictionary to store the count of each character
    char_count = {}

    # Iterate through each character in the string
    for char in input_str:
        # Increment the count for each character
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Iterate through the characters again to find the first non-repeating character
    for char in input_str:
        if char_count[char] == 1:
            return char

    # If no non-repeating character is found, return None
    return None