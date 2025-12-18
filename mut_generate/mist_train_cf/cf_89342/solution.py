"""
QUESTION:
Implement a function named `collapse_and_sort_string` that takes a string of lowercase alphabetic characters as input, and returns a new string where all repeating continuous characters are collapsed to a single character, and the output string is sorted in lexicographically increasing order, without using any additional data structures.
"""

def collapse_and_sort_string(input_str):
    output = ""
    prev_char = None
    
    for char in input_str:
        if char == prev_char:
            continue
        output += char
        prev_char = char
    
    return "".join(sorted(output))