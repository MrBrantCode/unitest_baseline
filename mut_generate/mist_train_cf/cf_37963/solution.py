"""
QUESTION:
Implement a function called `transform_string` that takes a single input string and returns a transformed string where each character in the input string is followed by its count. If a character appears multiple times in the input string, its count is incremented accordingly in the transformed string. The function should handle any type of character in the input string. The transformed string should be constructed by concatenating the character and its count for each unique character in the input string.
"""

def transform_string(input_string):
    char_count = {}
    
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return "".join(char + str(count) for char, count in char_count.items())