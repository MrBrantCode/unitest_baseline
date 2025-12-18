"""
QUESTION:
Write a function `find_odd_palindromes` that takes a list of strings `words` as input, where each string contains only lowercase letters (a-z) and has a length between 1 and 10^4. The function should return a list of strings representing all the palindrome words found in `words` that have an odd number of characters.
"""

def find_odd_palindromes(words):
    result = []
    for word in words:
        if len(word) % 2 != 0 and word == word[::-1]:
            result.append(word)
    return result