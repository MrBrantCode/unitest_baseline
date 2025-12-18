"""
QUESTION:
Write a function `most_frequent_character(string)` that takes a string of up to 100 characters as input, considering both uppercase and lowercase characters as the same, and returns the character with the highest frequency in the string. If there are multiple characters with the same highest frequency, the function should return any one of them.
"""

def most_frequent_character(string):
    string = string.lower()
    char_freq = {}
    for char in string:
        char_freq[char] = char_freq.get(char, 0) + 1
    max_freq = 0
    most_freq_char = ''
    for char, freq in char_freq.items():
        if freq > max_freq:
            max_freq = freq
            most_freq_char = char
    return most_freq_char