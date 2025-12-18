"""
QUESTION:
Write a function called `get_string_info` that takes a string as input. The function should return the total length of the string (excluding uppercase letters and non-alphabetic characters), the count of unique lowercase characters in the string, and a dictionary with the frequency of each unique lowercase character. The function should be case-insensitive and should not use any built-in length or string functions to calculate the length.
"""

def get_string_info(string):
    # Initialize variables
    length = 0
    unique_chars = set()
    char_count = {}

    # Convert string to lowercase
    string = string.lower()

    # Iterate over each character in the string
    for char in string:
        # Exclude non-alphabetic characters from length count
        if char.isalpha():
            if char.islower():
                length += 1

        # Exclude non-alphabetic characters from unique characters set
        if char.isalpha():
            if char.islower():
                unique_chars.add(char)

        # Count the frequency of each unique lowercase character
        if char.isalpha():
            if char.islower():
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1

    # Return length, unique characters count, and character frequency dictionary
    return length, len(unique_chars), char_count