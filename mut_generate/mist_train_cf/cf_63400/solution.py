"""
QUESTION:
Construct a Python function `count_char_freq` that takes a list of strings as input and returns a dictionary where the keys are unique characters and the values represent their frequency across all strings in the input list. The function should be case-sensitive and should count each occurrence of a character.
"""

def count_char_freq(list_of_strings):
    freq_count = {}
    for string in list_of_strings:
        for character in string:
            if character in freq_count:
                freq_count[character] += 1
            else:
                freq_count[character] = 1
    return freq_count