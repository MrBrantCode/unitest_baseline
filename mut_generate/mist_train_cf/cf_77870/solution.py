"""
QUESTION:
Create a function named `vowel_count` that takes a string `s` as input and returns the count of characters that meet the following conditions: 
- at even indices, the characters must be uppercase vowels ('A', 'E', 'I', 'O', 'U') or spaces.
- at odd indices, the characters must be lowercase vowels ('a', 'e', 'i', 'o', 'u') or spaces.
"""

def vowel_count(s):
    count = 0
    for i in range(len(s)):
        if i % 2 == 0: 
            if s[i] in 'AEIOU ': 
                count += 1
        else: 
            if s[i] in 'aeiou ': 
                count += 1
    return count