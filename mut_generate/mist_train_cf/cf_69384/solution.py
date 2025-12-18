"""
QUESTION:
Create a recursive function called `reverse_integer(n)` that takes an integer `n` as input and returns the integer with its digits reversed. The function should only use recursion to solve the problem, without using any loops or built-in string reversal functions. The input integer can be any positive integer.
"""

def reverse_integer(n):
    if n < 10:
        return n
    else:
        return int(str(n % 10) + str(reverse_integer(n // 10)))