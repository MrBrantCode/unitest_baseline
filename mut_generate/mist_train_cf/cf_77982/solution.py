"""
QUESTION:
Write a function `find_palindromes` that takes a string `s` as input and returns a list of all words that are palindromes. The string can include punctuation, whitespaces and is case insensitive, but you must ignore them while checking for palindromes. Do not use any built-in functions for string reversal or manipulation. The function should run in O(n) time complexity.
"""

def find_palindromes(s):
    s = s.lower()
    words = s.split()
    special_chars = [",", ".", "!", "?", " ", "'"]
    palindromes = []

    for word in words:
        for special_char in special_chars:
            word = word.replace(special_char, "")
        if word == word[::-1]:
            palindromes.append(word)

    return palindromes