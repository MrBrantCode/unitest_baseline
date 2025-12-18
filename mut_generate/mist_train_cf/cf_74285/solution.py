"""
QUESTION:
Write a function named `eliminate_repeats` that takes a string `s` as input and returns a new string where sequences of continuous repeated characters are removed. The function should add each character from the input string to the new string only if it is not the same as the previous character.
"""

def eliminate_repeats(s):
    new_s = ''
    for i in range(len(s)):
        # add character to new string only if it is not the same as previous character
        if i == 0 or s[i] != s[i-1]:
            new_s += s[i]
    return new_s