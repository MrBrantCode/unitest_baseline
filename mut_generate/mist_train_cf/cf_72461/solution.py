"""
QUESTION:
Create a function `char_freq_map(s)` that generates a dictionary with unique characters from a given string as keys and their respective occurrence frequency as values. The function should handle non-alphanumeric characters by using their Unicode value as key instead of the character itself, ignore case sensitivity, and treat whitespace characters as non-alphanumeric.
"""

def char_freq_map(s):
    # convert the string to lowercase to handle case insensitivity
    s = s.lower()

    # intended to produce a character frequency dictionary
    freq_dict = {}
    for char in s:
        # check if character is alphanumeric
        if char.isalnum():
            if char in freq_dict.keys():
                freq_dict[char] += 1
            else:
                freq_dict[char] = 1
        else:  # handle non-alphanumeric characters
            char_ord = ord(char)
            if char_ord in freq_dict.keys():
                freq_dict[char_ord] += 1
            else:
                freq_dict[char_ord] = 1

    return freq_dict