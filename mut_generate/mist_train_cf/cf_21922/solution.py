"""
QUESTION:
Write a function `find_longest_string_with_ordered_uppercase(strings)` that takes an array of strings as input. The function should return the longest string that contains at least one uppercase letter and has all uppercase letters in alphabetical order. If no such string exists, return an empty string.
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