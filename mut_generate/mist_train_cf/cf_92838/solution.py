"""
QUESTION:
Write a function called `find_max_occurrence` that takes a string `s` as input and returns the index of the alphanumeric character that appears the most in the string, ignoring case, special characters, and whitespaces. If multiple characters have the same maximum occurrence, return the index of the character that appears first in the string.
"""

def find_max_occurrence(s):
    # Remove special characters and whitespaces
    s = ''.join(c.lower() for c in s if c.isalnum())
    
    # Count the occurrences of each character
    char_counts = {}
    for i, c in enumerate(s):
        if c in char_counts:
            char_counts[c] += 1
        else:
            char_counts[c] = 1
    
    # Find the character with maximum occurrence
    max_occurrence = 0
    max_char = None
    for c, count in char_counts.items():
        if count > max_occurrence:
            max_occurrence = count
            max_char = c
    
    # Find the index of the character that appears first in the string
    max_index = None
    for i, c in enumerate(s):
        if c == max_char:
            max_index = i
            break
    
    return max_index