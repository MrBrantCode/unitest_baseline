"""
QUESTION:
Write a function `count_vowels` that takes a string as input and returns the count of vowels in the string, excluding any vowels that are followed immediately by a digit and preceded by a consonant, and excluding any vowels that are at the beginning or end of a word in the string. The function should ignore uppercase and lowercase distinctions and handle strings containing special characters, numbers, and whitespace.
"""

import re

def count_vowels(string):
    vowels = 'aeiou'
    count = 0
    words = re.findall(r'\b\w+\b', string)
    
    for word in words:
        word = word.lower()
        for i in range(len(word)):
            if word[i] in vowels:
                if i != 0 and i != len(word) - 1 and not word[i-1].isalpha() and word[i-1].lower() not in vowels and not word[i+1].isdigit():
                    count += 1
    
    return count