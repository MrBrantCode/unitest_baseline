"""
QUESTION:
Create a function named `longest_characters` that takes a string of alphabetical characters and spaces as input, and returns a string containing each unique character (in lowercase) followed by its frequency in the input string. The characters in the output string should be sorted in descending order of their frequencies.
"""

def longest_characters(string):
    string = string.replace(" ", "").lower()
    char_freq = {}
    for char in string:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    sorted_chars = sorted(char_freq.keys(), key=lambda x: char_freq[x], reverse=True)
    result = ""
    for char in sorted_chars:
        result += char + str(char_freq[char])
    return result