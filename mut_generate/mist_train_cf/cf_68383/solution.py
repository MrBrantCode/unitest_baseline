"""
QUESTION:
Write a function `pangram_check(phrase)` that determines whether a given phrase is a pangram, returning `True` if it is and `(False, missing_letters)` if it is not. The function should be case-insensitive, ignore punctuation and special characters, and identify missing letters at the earliest possible point. The `missing_letters` list should be sorted alphabetically.
"""

def pangram_check(phrase):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    phrase = ''.join(e for e in phrase if e.isalnum()).lower()
    phrase = set(phrase)
    
    missing_letters = list(alphabet - phrase)
    missing_letters.sort()
    if len(missing_letters) == 0:
        return True
    else:
        return (False, missing_letters)