"""
QUESTION:
Write a function `generate_strings(n)` that generates all possible strings of length `n` using the characters 'A', 'B', 'C', and 'D' without any consecutive repetition of the same letter and excluding strings that contain the substring 'CD'.
"""

from itertools import product

def generate_strings(n):
    letters = ['A', 'B', 'C', 'D']
    all_strings = product(letters, repeat=n)
    final_strings = []
    
    for string in all_strings:
        prev = None
        for letter in string:
            if letter == prev or 'CD' in ''.join(string):
                break
            prev = letter
        else:
            final_strings.append(''.join(string))
    
    return final_strings