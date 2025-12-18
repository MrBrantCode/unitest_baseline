"""
QUESTION:
Write a function `F(n)` that calculates the maximum number of squares Peter can move a token beyond the dividing line in a checkerboard game, where each square in the $d$th column to the left of the dividing line begins with $d^n$ tokens instead of $1$. The function should take an integer `n` as input and return an integer value. The calculation should be efficient enough to handle large values of `n`, such as `1234567`.
"""

def F(n):
    return n*(n+1)*(2*n+1)//6 - 1