"""
QUESTION:
Implement a function called `get_odd_collatz` that takes a positive integer `n` as input and returns a list of odd numbers in the Collatz sequence, in ascending order. The Collatz sequence is defined as follows: if the current term is even, the next term is half of it, and if the current term is odd, the next term is three times the current term plus 1. The sequence ends when it reaches 1.
"""

def get_odd_collatz(n):
    odds = set()
    while n != 1:
        if n % 2 != 0: 
            odds.add(n)
        n = n * 3 + 1 if n % 2 else n // 2
    odds.add(1)
    return sorted(list(odds))