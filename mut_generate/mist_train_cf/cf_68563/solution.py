"""
QUESTION:
Implement a function named `longest_substring` that takes an input string and returns the longest sequence of unique characters. The function must use a repetitive loop structure and ensure that its purpose remains intact. The longest sequence is defined as the longest string of characters that does not repeat any character.
"""

def longest_substring(input_string):
    max_str = current_str = ""
    for char in input_string:
        if char not in current_str:
            current_str += char
            if len(current_str) > len(max_str):
                max_str = current_str
        else:
            cut_position = current_str.index(char)
            current_str = current_str[cut_position+1:] + char
    return max_str