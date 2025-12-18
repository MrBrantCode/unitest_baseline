"""
QUESTION:
Write a function `find_palindromes(word)` that generates all unique palindromic permutations of a given input string. The function should return a set of all unique palindromic permutations. Assume the input string only contains uppercase letters.
"""

from itertools import permutations

def find_palindromes(word):
    palindromes = set()
    for p in permutations(word):
        p = ''.join(p)
        if p == p[::-1]:  # If the word is the same forwards and backwards
            palindromes.add(p)
    return palindromes