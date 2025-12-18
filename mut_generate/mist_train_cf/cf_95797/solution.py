"""
QUESTION:
Write a Python function named `count_valid_jokes` that takes a string as input and returns the number of valid jokes that can be created using the characters in the string, following these rules:
- The string must contain at least one vowel (a, e, i, o, u) and one consonant (any letter that is not a vowel).
- The string must have a length of at least 5 characters.
- The string must not contain any special characters or numbers.
- The string must have a minimum of 2 consonants and 2 vowels.
- The string must contain at least one word with a length of 3 or more characters.
- The string must not contain any repeated consecutive letters.
- The string must not contain any repeated consecutive vowels or consonants.
The function should return the total number of valid jokes that can be created, which is either 0 or 1.
"""

def count_valid_jokes(input_string):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"

    # Check for rule 1 and 2
    if not any(char.lower() in vowels for char in input_string) or not any(char.lower() in consonants for char in input_string):
        return 0

    # Check for rule 3
    if len(input_string) < 5:
        return 0

    # Check for rule 4
    if not input_string.isalpha():
        return 0

    # Check for rule 5
    vowel_count = 0
    consonant_count = 0
    for char in input_string:
        if char.lower() in vowels:
            vowel_count += 1
        elif char.lower() in consonants:
            consonant_count += 1

    if vowel_count < 2 or consonant_count < 2:
        return 0

    # Check for rule 6
    words = input_string.split()
    if not any(len(word) >= 3 for word in words):
        return 0

    # Check for rule 7
    for i in range(len(input_string) - 1):
        if input_string[i] == input_string[i + 1]:
            return 0

    # Check for rule 8
    for i in range(len(input_string) - 2):
        if (input_string[i].lower() in vowels and input_string[i + 1].lower() in vowels and input_string[i + 2].lower() in vowels) or (input_string[i].lower() in consonants and input_string[i + 1].lower() in consonants and input_string[i + 2].lower() in consonants):
            return 0

    return 1