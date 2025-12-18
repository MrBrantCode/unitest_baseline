"""
QUESTION:
Create a function called `count_letters(word)` that takes a string `word` containing a single English word as input and returns the number of letters in the word. The function must not use the built-in `len()` function.
"""

def count_letters(word):
    count = 0
    for letter in word:
        count += 1
    return count