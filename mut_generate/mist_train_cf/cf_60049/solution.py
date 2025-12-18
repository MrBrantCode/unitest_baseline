"""
QUESTION:
Write a function `spynum(n, sm=0, pd=1)` that takes an integer `n` and checks if the sum of its digits equals the product of its digits. The function should return a boolean value indicating whether the condition is met. The function should use recursion and handle cases where `n` is a multi-digit number.
"""

def spynum(n, sm=0, pd=1):
    if n == 0:
        return sm == pd
    else:
        rem = n % 10
        sm += rem
        pd *= rem
        return spynum(n//10, sm, pd)