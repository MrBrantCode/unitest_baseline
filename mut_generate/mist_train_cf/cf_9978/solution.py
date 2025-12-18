"""
QUESTION:
Write a function `first_repeated_letter(string)` that finds the first occurrence of a repeated letter in the given string and returns its index. If no repeated letter is found, return -1.
"""

def first_repeated_letter(string):
    letter_count = {}
    
    for i, letter in enumerate(string):
        if letter in letter_count:
            return i
        else:
            letter_count[letter] = 1
    
    return -1