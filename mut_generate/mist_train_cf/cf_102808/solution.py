"""
QUESTION:
Write a function named `count_down` that takes one integer argument `n`. The function should recursively print numbers from `n` down to 1 without causing a stack overflow error.
"""

def count_down(n):
    if n == 0:
        return
    else:
        print(n)
        count_down(n-1)