"""
QUESTION:
Write a recursive function `reverse_numbers(n)` that generates a list of numbers from 1 to `n` in reverse order, without using any loop constructs. The function should only use recursive calls.
"""

def entrance(n):
    if n == 1:
        return [n]
    else:
        return [n] + entrance(n-1)