"""
QUESTION:
Write a function `character_occurrence` that takes a string of text as input and outputs the occurrence rate of each distinctive character within the string, considering both lower and upper case characters as distinct.
"""

def character_occurrence(string):
    count = {}
    for character in string:
        if character in count:
            count[character] += 1
        else:
            count[character] = 1
    return count