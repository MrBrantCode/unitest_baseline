"""
QUESTION:
Develop a function named `find_palindromes` that takes a string of text as input and returns a dictionary where the keys are unique palindromes found in the text, excluding single-character palindromes, and the values are the counts of each palindrome. The function should efficiently handle large text inputs and consider each word individually, ignoring punctuation and not considering palindromes spanning multiple words.
"""

from collections import Counter

def find_palindromes(text):
    words = text.split()
    palindromes = Counter()

    for word in words:
        if word == word[::-1] and len(word) > 1:
            palindromes[word] += 1

    return dict(palindromes)