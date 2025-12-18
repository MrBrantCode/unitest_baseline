"""
QUESTION:
Create a function `vowels_count` that accepts a string representing a word and returns the total number of vowels present. Vowels include 'a', 'e', 'i', 'o', 'u', and 'y' only when it appears as the last letter of the word. The function should ignore case and account for special characters.
"""

def vowels_count(s):
    s = s.lower()
    count = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for i in range(len(s)):
        if s[i] in vowels:
            count += 1
        if s[i] == 'y' and i == len(s) - 1:
            count += 1
    return count