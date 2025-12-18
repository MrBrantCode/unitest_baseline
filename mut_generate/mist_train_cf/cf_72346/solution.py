"""
QUESTION:
Write a function named `find_character` that determines if a given character is present in a word, considering case sensitivity and special characters, and returns the index of the character if it exists. If the character is not found, the function should return a message indicating so. The function should take two parameters: `word` and `character`.
"""

def find_character(word, character):
    if character in word:
        return word.index(character)
    else:
        return "Character not found in the word"