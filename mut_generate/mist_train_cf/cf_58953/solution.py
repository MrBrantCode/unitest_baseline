"""
QUESTION:
Write a function called `remove_elements_and_repeats` that takes a string `text` as input and returns a new string containing only the unique consonants from the original string. The function should exclude vowels, digits, punctuation, and repeated consonants from the output.
"""

import re
def remove_elements_and_repeats(text):
    result = ''
    seen = set()
    
    text = re.sub('[aeiou0-9\W_]', '', text.lower()) # removing vowels, digits, and punctuation
    
    # removing repeated consonants
    for char in text:
        if char not in seen:
            seen.add(char)
            result += char
    return result