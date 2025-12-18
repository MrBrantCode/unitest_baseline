"""
QUESTION:
Create a function `process_strings` that takes a list of strings as input, removes any strings containing special characters or numbers (except spaces), converts the remaining strings to lowercase, removes duplicates, sorts them alphabetically, and counts the occurrences of each string. The function should return the sorted list of strings along with their respective counts. 

Restrictions: 
- Special characters are defined as non-alphabetic characters except for spaces.
- Numbers are also considered as special characters.
- The function should ignore case sensitivity when comparing strings.
- The function should handle duplicate strings.
"""

import re

def process_strings(strings):
    # Convert strings to lowercase and remove special characters and numbers
    strings = [re.sub(r'[^a-zA-Z\s]', '', string.lower()) for string in strings]

    # Remove duplicates and sort strings alphabetically
    unique_strings = sorted(set(strings))

    # Count the occurrences of each string
    counts = {string: strings.count(string) for string in unique_strings}

    return [(string, counts[string]) for string in unique_strings]