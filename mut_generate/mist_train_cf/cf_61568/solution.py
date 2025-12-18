"""
QUESTION:
Create a function `purify_text(text)` that takes a string `text` as input, removes all vowels, numbers, and special characters, and eliminates duplicate occurrences of consonants while preserving the original order of characters. The function should be case-sensitive, treating uppercase and lowercase consonants as distinct characters.
"""

def purify_text(text):
    seen = set()
    result = []

    for char in text:
        # Check character is a consonant: Not a digit and not a vowel
        if char.isalpha() and char.lower() not in 'aeiou':
            # Seen for the first time
            if char.lower() not in seen:
                seen.add(char.lower())
                result.append(char)
        elif char.isalpha() and char.lower() in 'aeiou':
            continue    # Ignoring vowels
        else:
            continue    # Ignoring numbers and special characters

    return ''.join(result)