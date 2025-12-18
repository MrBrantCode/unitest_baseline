"""
QUESTION:
Write a function `count_uppercase` that takes a string as input and returns the count of uppercase characters in the string. The input string should contain at least one lowercase character and at most 100 characters.
"""

def count_uppercase(string):
    count = 0
    for char in string:
        if char.isupper():
            count += 1
    return count