"""
QUESTION:
Design a function called `count_upper` that takes one string argument and returns the number of capital vowel letters ('A', 'E', 'I', 'O', 'U') that are exactly at even indices in the string. The function should return an error message 'Invalid input' if the input is not a string.
"""

def count_upper(s):
    if not isinstance(s, str):
        return 'Invalid input'
    vowel_list = ['A', 'E', 'I', 'O', 'U']
    return sum([1 for i in range(len(s)) if s[i] in vowel_list and i % 2 == 0])