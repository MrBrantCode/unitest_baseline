"""
QUESTION:
Write a function `at_least_two_in_codeforces(chars)` that takes a list of three characters as input and returns True if at least two of them appear in the string "codeforces", and False otherwise.
"""

def at_least_two_in_codeforces(chars):
    count = 0
    for char in chars:
        if char in 'codeforces':
            count += 1
    return count >= 2