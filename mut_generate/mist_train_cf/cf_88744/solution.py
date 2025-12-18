"""
QUESTION:
Write a function `valid_jokes_count` that takes in a string `s` as input and returns the number of valid jokes that can be created using the characters in the input string, following these rules:

- The string must contain at least one vowel and one consonant.
- The string must have a length of at least 10 characters and contain only letters and spaces.
- The string must have a minimum of 3 consonants and 3 vowels.
- The string must contain at least two words with a length of 4 or more characters.
- The string must not contain any repeated consecutive letters, vowels, or consonants.
- The string must have at least one uppercase letter and one lowercase letter.
"""

import re

def valid_jokes_count(s):
    # Rule 1: The string must contain at least one vowel (a, e, i, o, u).
    if not re.search('[aeiou]', s):
        return 0

    # Rule 2: The string must contain at least one consonant (any letter that is not a vowel).
    if not re.search('[bcdfghjklmnpqrstvwxyz]', s):
        return 0

    # Rule 3: The string must have a length of at least 10 characters.
    if len(s) < 10:
        return 0

    # Rule 4: The string must not contain any special characters or numbers.
    if not re.match('^[a-zA-Z ]*$', s):
        return 0

    # Rule 5: The string must have a minimum of 3 consonants and 3 vowels.
    consonants_count = len(re.findall('[bcdfghjklmnpqrstvwxyz]', s))
    vowels_count = len(re.findall('[aeiou]', s))
    if consonants_count < 3 or vowels_count < 3:
        return 0

    # Rule 6: The string must contain at least two words with a length of 4 or more characters.
    words = s.split()
    long_words_count = len([word for word in words if len(word) >= 4])
    if long_words_count < 2:
        return 0

    # Rule 7: The string must not contain any repeated consecutive letters.
    if re.search(r'([a-zA-Z])\1', s):
        return 0

    # Rule 8: The string must not contain any repeated consecutive vowels or consonants.
    if re.search(r'([aeiou])\1', s) or re.search(r'([bcdfghjklmnpqrstvwxyz])\1', s):
        return 0

    # Rule 9: The string must have at least one uppercase letter and one lowercase letter.
    if not re.search('[a-z]', s) or not re.search('[A-Z]', s):
        return 0

    # All rules satisfied, return 1
    return 1