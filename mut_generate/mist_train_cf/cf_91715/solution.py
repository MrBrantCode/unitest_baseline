"""
QUESTION:
Write a function `longest_string_with_letters` that takes a list of strings as input and returns the longest string that contains at least one uppercase letter and one lowercase letter. The function should return the first longest string it encounters in case of a tie.
"""

def longest_string_with_letters(strings):
    longest_string = ''
    for string in strings:
        if any(c.islower() for c in string) and any(c.isupper() for c in string):
            if len(string) > len(longest_string):
                longest_string = string
    return longest_string