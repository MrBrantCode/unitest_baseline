"""
QUESTION:
Write a function named `find_longest_string` that takes an array of strings as input. The function should return a tuple containing the longest string that contains at least one uppercase letter and has its uppercase letters in alphabetical order, and the number of uppercase letters in that string.
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