"""
QUESTION:
Write a function `find_character` that takes a string and a lowercase alphabet character as input and returns the first index at which the character appears in the string. The function should not use any built-in string or array methods and should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the string. If the character is not found, return -1.
"""

def find_character(string, character):
    for i in range(len(string)):
        if string[i] == character:
            return i
    return -1  # character not found in the string