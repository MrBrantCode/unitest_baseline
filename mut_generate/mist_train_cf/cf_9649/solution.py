"""
QUESTION:
Write a function named `count_characters` that takes a string as input and returns the number of non-whitespace characters in the string, treating uppercase and lowercase letters as distinct characters.
"""

def count_characters(string):
    count = 0
    for char in string:
        if char != " ":
            count += 1
    return count