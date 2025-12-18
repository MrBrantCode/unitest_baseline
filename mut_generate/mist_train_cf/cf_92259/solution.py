"""
QUESTION:
Write a function called `count_jokes` that takes a string as input and returns the number of valid jokes that can be formed using the characters in the string. A valid joke must be at least 5 characters long, contain at least one vowel (a, e, i, o, u) and one consonant, and only contain letters. If the string meets these conditions, the function should return 1; otherwise, it should return 0.
"""

def count_jokes(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = [chr(i) for i in range(ord('a'), ord('z')+1) if chr(i) not in vowels]

    # Check if the string is at least 5 characters long
    if len(input_string) < 5:
        return 0

    # Check if the string contains at least one vowel and one consonant
    has_vowel = any(char.lower() in vowels for char in input_string)
    has_consonant = any(char.lower() in consonants for char in input_string)

    if not has_vowel or not has_consonant:
        return 0

    # Check if the string contains any special characters or numbers
    for char in input_string:
        if not char.isalpha():
            return 0

    # If all conditions are met, return 1
    return 1