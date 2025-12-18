"""
QUESTION:
Create a function `get_character_frequency` that takes a string `str` as input and returns a dictionary where the keys are the characters in the string and the values are the frequencies of each character, regardless of case. The function should be case sensitive and include non-alphabet characters in the frequency count. The dictionary keys should include spaces and punctuation.
"""

def get_character_frequency(str):
    char_freq = {}
    for char in str:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    return char_freq