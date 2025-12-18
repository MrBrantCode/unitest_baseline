"""
QUESTION:
Create a function `count_lower(s)` that takes a string `s` as input and returns the frequency of lowercase consonants located at odd-indexed positions. Assume that indexing starts at 0, so the first character is at an even index. The function should ignore non-alphabetic characters, uppercase letters, and lowercase vowels.
"""

def count_lower(s):
    vowels = 'aeiou'
    sum = 0
    for i in range(len(s)):
        if i % 2 == 1 and s[i].islower() and s[i] not in vowels:
            sum += 1
    return sum