"""
QUESTION:
Create a function named `remove_vowels` that takes two parameters: `sentence` and an optional `exclude_y` parameter (defaulting to `True`). The function should return the input `sentence` with all vowels removed, preserving the original casing and punctuation. If `exclude_y` is `False`, 'y' should also be considered a vowel and removed.
"""

def remove_vowels(sentence, exclude_y=True):
    vowels = 'aeiou'
    if not exclude_y:
        vowels += 'y'
    return ''.join([char for char in sentence if char.lower() not in vowels])