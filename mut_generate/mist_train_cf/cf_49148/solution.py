"""
QUESTION:
Create a function named `count_upper` that takes a string `s` as input and returns the number of uppercase vowels ('A', 'E', 'I', 'O', 'U') present only at even indices in the string.
"""

def count_upper(s):
    uppercase_vowels = ['A', 'E', 'I', 'O', 'U']
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in uppercase_vowels:
            count += 1
    return count