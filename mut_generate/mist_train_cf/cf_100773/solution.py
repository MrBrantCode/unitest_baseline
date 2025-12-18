"""
QUESTION:
Write a function `at_least_two_in_codeforces(chars)` that determines if at least two of three given characters appear in the string "codeforces". The input `chars` is a list or iterable of characters.
"""

def at_least_two_in_codeforces(chars):
    count = 0
    for char in chars:
        if char in 'codeforces':
            count += 1
    return count >= 2