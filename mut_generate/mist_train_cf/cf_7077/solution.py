"""
QUESTION:
Write a function named `find_odd_palindromes` that takes a list of strings `words` as input, where each string contains only lowercase letters (a-z). The function should return a list of strings representing all the palindrome words found in `words` that have an odd number of characters. The words should be sorted in descending order based on their lengths. The length of the input list `words` will be between 1 and 10^4.
"""

from typing import List

def find_odd_palindromes(words: List[str]) -> List[str]:
    palindrome_words = [word for word in words if len(word) % 2 == 1 and word == word[::-1]]
    palindrome_words.sort(key=lambda x: len(x), reverse=True)
    return palindrome_words