"""
QUESTION:
Write a function `find_term(a, n)` that calculates the nth term of a geometric progression series, where `a` is the first term and `n` is the position of the term. The series has a common ratio of 2, meaning each term is double the preceding term.
"""

def find_term(a, n):
    return a * (2 ** (n-1))