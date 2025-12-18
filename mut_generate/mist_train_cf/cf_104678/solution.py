"""
QUESTION:
Create a function called `remove_whitespace_duplicates` that takes a string as input and returns a modified string with all whitespace characters removed and no duplicate characters, preserving the original order of characters. The function should not use any external libraries or built-in string methods other than `isspace()` and `join()`.
"""

def remove_whitespace_duplicates(string):
    unique_characters = []
    characters_list = list(string)
    for char in characters_list:
        if char.isspace():
            continue
        if char not in unique_characters:
            unique_characters.append(char)
    result_string = ''.join(unique_characters)
    return result_string