"""
QUESTION:
Write a function `third_unique_char` that takes a string `phrase` as input and returns the third unique character in the string. If the string does not have three unique characters, return the error message "not enough unique characters". The function should be case-sensitive.
"""

def third_unique_char(phrase):
    unique_chars = []
    for c in phrase:
        if c not in unique_chars:
            unique_chars.append(c)
        if len(unique_chars) == 3:
            return unique_chars[2]
    
    return "Error: not enough unique characters"