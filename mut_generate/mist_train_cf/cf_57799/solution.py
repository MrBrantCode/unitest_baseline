"""
QUESTION:
Create a function `check_char(character)` that takes a single character as input. The function should return a string indicating whether the character is a vowel or a consonant. The function should also handle invalid inputs by returning error messages for non-alphabetical characters and inputs with multiple characters.
"""

def check_char(character):
    vowels = 'aeiou'
    if len(character) > 1:
        return "Error: Input string must be a single character."
    elif not character.isalpha():
        return "Error: Input character must be an alphabet."
    else:
        if character.lower() in vowels:
            return "The input character is a vowel."
        else:
            return "The input character is a consonant."