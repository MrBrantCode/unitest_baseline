"""
QUESTION:
Develop a function named `count_palindromes` that takes two parameters: a string `text` and an integer `min_length`. This function should count the occurrence of unique palindromes in the given `text` with a length of at least `min_length`, considering punctuation and multilanguage support, including accented characters. The function should also provide a running tally of palindrome counts. The function should return a dictionary where keys are palindromes in the text and values are their corresponding counts.
"""

from collections import Counter
import re
import unicodedata

def count_palindromes(text, min_length):
    palindromes_count = Counter()

    def clean_word(word):
        nfkd_form = unicodedata.normalize('NFKD', word).encode('ASCII', 'ignore').decode()
        return nfkd_form.lower()

    def is_palindrome(word):
        word = clean_word(word)
        return word == word[::-1]

    words = re.findall(r'\b\w+\b', text)
    for word in words:
        if len(word) >= min_length and is_palindrome(word):
            palindromes_count.update([word])
    return palindromes_count