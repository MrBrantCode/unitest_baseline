"""
QUESTION:
Write a function `max_digit_removal(n)` that takes a positive integer `n` and returns the maximum possible integer that can be obtained by removing exactly one digit from `n`.
"""

def max_digit_removal(n):
    s = str(n)  
    return max(int('{}{}'.format(s[:i], s[i+1:])) for i in range(len(s)))