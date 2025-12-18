"""
QUESTION:
Write a function `find_longest_string_with_ordered_uppercase(strings)` that takes a list of strings as input and returns the longest string from the list where the uppercase letters in the string are in alphabetical order and the string contains at least one uppercase letter. If there are multiple strings with the same maximum length, return the first one encountered.
"""

def find_longest_string_with_ordered_uppercase(strings):
    longestString = ""

    for string in strings:
        if any(char.isupper() for char in string):
            if len(string) > len(longestString):
                uppercase_letters = [char for char in string if char.isupper()]
                if uppercase_letters == sorted(uppercase_letters):
                    longestString = string

    return longestString