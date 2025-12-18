"""
QUESTION:
Write a function `collapse_string` that takes a string of lowercase alphabetic characters as input, removes consecutive duplicate characters, and returns a new string with the remaining characters in lexicographically increasing order.
"""

def collapse_string(input_str):
    result = ''
    prev_char = ''
    
    for char in input_str:
        if char != prev_char:
            result += char
        prev_char = char
    
    return ''.join(sorted(result))