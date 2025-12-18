"""
QUESTION:
Write a function `delete_duplicates` that takes a string as input and returns a new string with all duplicate characters removed, preserving the original order of characters.
"""

def delete_duplicates(string):
    letters = set()
    newstring = ""
    for char in string:
        if char in letters:
            continue
        else:
            letters.add(char)
            newstring += char
    return newstring