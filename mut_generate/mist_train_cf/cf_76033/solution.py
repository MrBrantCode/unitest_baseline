"""
QUESTION:
Write a function `remove_nonalpha_length` that takes a string composed of lowercase letters, whitespace, and punctuation marks as input and returns the length of the string excluding whitespace and punctuation marks. The input string can be of any length and may contain any combination of lowercase letters, whitespace, and punctuation marks.
"""

def remove_nonalpha_length(input_string):
    return len(''.join(e for e in input_string if e.isalpha()))