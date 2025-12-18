"""
QUESTION:
Implement a function `count_vowels(word)` that takes a string `word` as input. The function should return the number of vowels in `word` if it is a valid English word; otherwise, return -1. A valid English word must meet the following criteria: have at least 6 characters, not start or end with a vowel, and not contain any consecutive vowels.
"""

def count_vowels(word):
    vowels = "aeiou"
    
    # Check if the word has at least 6 characters
    if len(word) < 6:
        return -1
    
    # Check if the word starts or ends with a vowel
    if word[0] in vowels or word[-1] in vowels:
        return -1
    
    # Check if the word contains consecutive vowels
    for i in range(len(word) - 1):
        if word[i] in vowels and word[i + 1] in vowels:
            return -1
    
    # Count the number of vowels in the word
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    
    return count