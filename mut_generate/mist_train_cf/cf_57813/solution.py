"""
QUESTION:
Create a function `count_upper(s)` that calculates the number of uppercase vowels at even indices in a string `s`, excluding the first and last character. The string `s` only contains alphabets. The function should return the total count of uppercase vowels at even indices.
"""

def count_upper(s):
    vowels = "AEIOU"
    return sum(s[i] in vowels for i in range(1, len(s)-1) if i % 2 == 0)