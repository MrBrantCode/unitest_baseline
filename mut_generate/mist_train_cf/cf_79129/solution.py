"""
QUESTION:
Write a function named `alphabeticCharacterCount` that takes a string as input and returns the number of alphabetic characters in the string, excluding whitespace and punctuation. The function should only count letters (both lowercase and uppercase) and ignore all other characters.
"""

def alphabeticCharacterCount(inputString):
    count = 0
    for character in inputString:
        if character.isalpha():
            count += 1
    return count