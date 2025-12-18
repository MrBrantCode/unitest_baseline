"""
QUESTION:
Write a function named `longest_consecutive_character` that takes a string as input and returns the character that has the longest consecutive repetition and its corresponding length in the string.
"""

def longest_consecutive_character(s):
    max_char = s[0]
    max_length = 1
    cur_length = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            cur_length += 1
            
            if cur_length > max_length:
                max_char = s[i]
                max_length = cur_length
        else: 
            cur_length = 1
    
    return max_char, max_length