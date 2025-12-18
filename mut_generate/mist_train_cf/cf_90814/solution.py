"""
QUESTION:
Write a function `get_third_character(word)` that takes a string `word` as input and returns the third character in the string using a single loop iteration and without using any built-in functions or libraries other than `len()` and `range()`. Assume the input string has at least three characters.
"""

def get_third_character(word):
    for i in range(len(word)):
        if i == 2:
            return word[i]