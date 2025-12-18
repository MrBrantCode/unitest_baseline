"""
QUESTION:
Write a function `check_conditions` that takes a string of length 10 as input and returns True if the string contains at least two 'a's, contains both 'b' and 'c', and 'b' appears before 'c'. The string is composed of characters 'a', 'b', 'c', and 'd'.
"""

def check_conditions(s):
    if s.count('a') < 2:
        return False
    if 'b' not in s or 'c' not in s:
        return False
    if s.index('b') > s.index('c'):
        return False
    return True