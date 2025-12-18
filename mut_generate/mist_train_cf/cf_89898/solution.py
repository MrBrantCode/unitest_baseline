"""
QUESTION:
Implement a function named `count_vowels` that takes a word as input. The word is valid if it meets the following conditions: it has at least 6 characters, does not start or end with a vowel, and does not contain any consecutive vowels. If the word is valid, return the number of vowels in the word; otherwise, return -1. The vowels are defined as "aeiou".
"""

def entrance(word):
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