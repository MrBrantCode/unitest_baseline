"""
QUESTION:
Write a function `count_upper(s)` that takes a string `s` as input and returns the frequency of uppercase vowels present at even numerical positions in the string. The function should only consider the characters at positions 0, 2, 4, and so on. Uppercase vowels include 'A', 'E', 'I', 'O', and 'U'.
"""

def count_upper(s):
    vowels = 'AEIOU'
    return sum(1 if s[i] in vowels else 0 for i in range(len(s)) if i%2 == 0)