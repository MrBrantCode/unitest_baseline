"""
QUESTION:
Given two strings `s` and `t`, write a function `process_strings(s, t)` that replaces all occurrences of characters in `t` in `s` with '*', then checks if the resultant string has any repeated characters, and returns a list containing the transformed string, a string showing the frequency count of each character in the transformed string, and "Unique" if all characters are unique or "Non-unique" otherwise.
"""

from collections import Counter

def process_strings(s, t):
    # Replace characters in t in s with '*'
    transformed = ''.join('*' if c in t else c for c in s)
    # Get frequency count of each character
    freq = Counter(transformed)
    # Build frequency count string
    freq_str = ','.join(f'{char}:{count}' for char, count in freq.items())
    # Check if all characters in result string are unique or not
    status = 'Unique' if all(value == 1 for value in freq.values()) else 'Non-unique'
    return [transformed, freq_str, status]