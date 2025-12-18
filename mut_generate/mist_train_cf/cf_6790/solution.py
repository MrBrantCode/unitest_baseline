"""
QUESTION:
Write a function called `get_string_info` that takes a string as input and returns the length of the string (excluding uppercase letters), the number of unique lowercase characters, and a dictionary with the frequency of each unique lowercase character. The function should not be case-sensitive and should exclude uppercase letters from the count of unique characters.
"""

def get_string_info(string):
    # Convert string to lowercase
    string = string.lower()

    # Initialize variables
    length = sum(1 for char in string if char.islower())
    unique_chars = set(char for char in string if char.islower())
    char_count = {char: string.count(char) for char in unique_chars}

    # Return length, unique characters count, and character frequency dictionary
    return length, len(unique_chars), char_count