"""
QUESTION:
Write a recursive function `lucas_seq(n)` that computes the nth term of the Lucas sequence, where the sequence is defined as: 
- lucas_seq(0) = 2
- lucas_seq(1) = 1
- lucas_seq(n) = lucas_seq(n-1) + lucas_seq(n-2) for n > 1. 

The function should use memoization to avoid redundant computation and should work for n up to 50.
"""

# Create a dictionary to store computed terms
lucas_dict = {0: 2, 1: 1}

def lucas_seq(n):
    if n in lucas_dict:
        return lucas_dict[n]
    else:
        lucas_dict[n] = lucas_seq(n-1) + lucas_seq(n-2)
        return lucas_dict[n]