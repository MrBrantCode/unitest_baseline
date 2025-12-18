"""
QUESTION:
Write a function `longest_substring(input_string)` that returns the length of the longest consecutive sequence of a single, distinct character in the input string, along with the character itself and the position of its first occurrence. The function should handle cases where a single, unique character forms the longest repeating sequence and accommodate input strings containing emojis. The function should use iterative loops instead of recursion.
"""

def longest_substring(input_string):
    max_len = 0
    max_char = ''
    cur_len = 0
    cur_char = ''
    pos = 0
    max_pos = 0

    for i, char in enumerate(input_string):
        if char == cur_char:
            cur_len += 1
        else:
            if cur_len > max_len:
                max_len = cur_len
                max_char = cur_char
                max_pos = pos
                
            cur_char = char
            cur_len = 1
            pos = i

    if cur_len > max_len:
        max_len = cur_len
        max_char = cur_char
        max_pos = pos

    return max_len, max_char, max_pos