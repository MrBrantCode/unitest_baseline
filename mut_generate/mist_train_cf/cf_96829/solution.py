"""
QUESTION:
Create a function named `is_valid_word` that takes a string `word` as input and returns the number of vowels in the word if it's a valid English word; otherwise, return -1. A valid English word must have at least 6 characters and cannot contain any consecutive vowels. The function should consider both lowercase and uppercase vowels as valid.
"""

def is_valid_word(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    word = word.lower()

    if len(word) < 6:
        return -1

    count = 0
    prev = word[0]
    for c in word[1:]:
        if c in vowels and prev in vowels:
            return -1
        if c in vowels:
            count += 1
        prev = c

    return count