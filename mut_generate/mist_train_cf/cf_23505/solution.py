"""
QUESTION:
Create a function `max_repeated_char` that takes a string `input_string` as input and returns the most frequently occurring character in the string. The function should ignore the frequency of spaces and consider only alphanumeric characters. If multiple characters have the same maximum frequency, the function should return any one of them.
"""

def max_repeated_char(input_string):
    char_count = dict()
    max_count = 0
    max_char = None
    for char in input_string:
        if char.isalnum():  # ignore non-alphanumeric characters
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1
            
    for char in char_count:
        if char_count[char] > max_count:
            max_count = char_count[char]
            max_char = char
    return max_char