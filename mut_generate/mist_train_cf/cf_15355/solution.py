"""
QUESTION:
Write a function `count_occurrences` that takes a string and a character as input. Return the number of occurrences of the character in the string, treating uppercase and lowercase characters as distinct entities.
"""

def count_occurrences(string, character):
    count = 0
    for char in string:
        if char == character:
            count += 1
    return count