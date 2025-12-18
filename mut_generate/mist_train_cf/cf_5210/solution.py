"""
QUESTION:
Write a function `third_to_last_character` that accepts a string as input and returns the third character from the end without using indexing or slicing to directly access the characters in the string. The function should work for strings of any length greater than or equal to 3.
"""

def third_to_last_character(string):
    characters = list(string)  # convert the string into a list of characters
    characters.reverse()  # reverse the list of characters
    return characters[2]  # access the third element