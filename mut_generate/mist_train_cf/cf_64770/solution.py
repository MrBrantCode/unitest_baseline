"""
QUESTION:
Create a function `remove_duplicate_chars` that takes a string `s` as input and returns a new string with all characters that appear more than once in `s` removed. The function should be case-sensitive and should not remove spaces.
"""

def remove_duplicate_chars(s):
    char_freq = {}
    result = ''

    # Get character frequencies.
    for char in s:
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] += 1

    # Construct new string with characters that only appear once.
    for char in s:
        if char_freq[char] == 1:
            result += char

    return result