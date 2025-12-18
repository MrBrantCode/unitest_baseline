"""
QUESTION:
Write a function `find_longest_string(strings)` that takes an array of strings as input and returns a tuple containing the longest string with at least one uppercase letter where all uppercase letters are in alphabetical order, and the number of uppercase letters in that string. If no such string exists, return an empty string and 0.
"""

def find_longest_string(strings):
    longest_string = ""
    longest_string_length = 0
    longest_string_uppercase_count = 0

    for string in strings:
        uppercase_count = sum(1 for char in string if char.isupper())

        if uppercase_count > 0 and len(string) > longest_string_length:
            uppercase_chars = [char for char in string if char.isupper()]
            if uppercase_chars == sorted(uppercase_chars):
                longest_string = string
                longest_string_length = len(string)
                longest_string_uppercase_count = uppercase_count

    return longest_string, longest_string_uppercase_count