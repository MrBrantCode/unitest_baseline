"""
QUESTION:
Write a function `collapse_string` that takes a string of lowercase alphabetic characters as input, removes consecutive repeating characters, and returns the resulting string in lexicographically increasing order. The function should only keep the first occurrence of each repeating character and maintain the original order of characters.
"""

def collapse_string(input_str):
    result = ''
    prev_char = ''
    
    for char in input_str:
        if char != prev_char:
            result += char
        prev_char = char
    
    return ''.join(sorted(result))