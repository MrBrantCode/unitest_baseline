"""
QUESTION:
Create a function named `count_upper_vowels` that takes a string `s` as input and returns the count of uppercase vowels ('A', 'E', 'I', 'O', 'U') at even index positions in the string (0-based indexing).
"""

def count_upper_vowels(s):
    counter = 0
    for i in range(len(s)):
        if i % 2 == 0 and s[i] in 'AEIOU': 
            counter += 1
    return counter