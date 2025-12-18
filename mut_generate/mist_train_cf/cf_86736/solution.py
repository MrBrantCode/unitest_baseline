"""
QUESTION:
Create a function named `replace_phrase` that takes three parameters: `string`, `phrase`, and `new_phrase`. The function should replace all occurrences of the specified `phrase` in the `string` with the `new_phrase`, but only if the `phrase` is a complete word. The function should ignore case sensitivity and not replace the `phrase` if it appears as a substring of another word.
"""

import re

def replace_phrase(string, phrase, new_phrase):
    pattern = r'\b{}\b'.format(phrase)
    new_string = re.sub(pattern, new_phrase, string, flags=re.IGNORECASE)
    return new_string