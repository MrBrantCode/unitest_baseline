"""
QUESTION:
Detect Capital Usage

Implement a function named `detectCapitalUse` that determines if the capitalization of a given word conforms to the rules of proper capital usage. The rules state that a word is properly capitalized if it meets one of the following conditions:
- All characters are capitalized.
- No characters are capitalized.
- Only the first character is capitalized, and the rest are lowercase.

The input word will be a non-empty string composed of uppercase and lowercase Latin alphabets.
"""

def detectCapitalUse(word: str) -> bool:
    return word.isupper() or word.islower() or word.istitle()