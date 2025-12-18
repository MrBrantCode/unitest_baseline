"""
QUESTION:
Write a function called `count_special_characters` that takes a string as input and returns a dictionary where the keys are unique special characters and the values are their frequencies. A special character is defined as any character that is not a letter, digit, or space.
"""

def count_special_characters(string):
    special_characters = {}

    for character in string:
        if not (character.isalpha() or character.isdigit() or character.isspace()):
            if character in special_characters:
                special_characters[character] += 1
            else:
                special_characters[character] = 1

    return special_characters