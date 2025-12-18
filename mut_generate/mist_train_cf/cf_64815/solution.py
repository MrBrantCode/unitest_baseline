"""
QUESTION:
Create a function `find_most_frequent_char` that takes an input string and returns the character that appears most frequently. The function should be case-insensitive, i.e., 'A' and 'a' are considered the same character. If there are multiple characters with the same highest frequency, the function can return any of them.
"""

def find_most_frequent_char(input_string):
    char_frequency = {}
    for char in input_string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    most_frequent_char = max(char_frequency, key = char_frequency.get)
    return most_frequent_char