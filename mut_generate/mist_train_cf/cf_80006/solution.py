"""
QUESTION:
Write a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string, ignoring case and special characters. Consider 'y' as a vowel only when it is at the end of the string.
"""

def vowels_count(s):
    s = s.lower()
    count = 0
    for char in s:
        if char in 'aeiou':
            count += 1
        elif char == 'y' and s.index(char) == len(s) - 1:
            count += 1
    return count