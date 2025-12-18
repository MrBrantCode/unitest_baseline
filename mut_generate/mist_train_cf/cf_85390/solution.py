"""
QUESTION:
Create a function named `character_count` that takes a string as input and returns a dictionary containing the count of each unique alphabetical character in the string. The function should be case-insensitive and ignore non-alphabetical characters, including special characters and spaces.
"""

def character_count(text):
    result = {}
    for character in text:
        # Only process alphabets
        if character.isalpha():
            # Make the character lower-case
            character = character.lower()
            result[character] = result.get(character, 0) + 1
    return result