"""
QUESTION:
Write a function `palindrome_frequency(text)` that takes a string `text` as input and returns the frequency of palindromes within the given text. The function should consider a word as a palindrome if it reads the same backward as forward, and it should be case insensitive.
"""

def palindrome_frequency(text):
    # convert the text to lowercase and split into individual words
    words = text.lower().split()
    # initialize the counter for palindromes
    count = 0
    for word in words:
        # check if the word is a palindrome
        if word == word[::-1]:
            # increase the counter
            count += 1
    return count