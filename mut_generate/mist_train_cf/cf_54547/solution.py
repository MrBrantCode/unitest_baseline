"""
QUESTION:
Write a function `modified_fib(n)` to calculate the nth number in a modified Fibonacci sequence where each number is the sum of the three preceding ones. The function should be able to handle large values of n efficiently, with a time complexity better than O(n) if possible. The input is a non-negative integer `n`, and the output is the nth number in the sequence.
"""

def modified_fib(n):
    if n < 0:
        return 
    a, b, c = 0, 1, 1
    if n == 0:
        return a 
    if n == 1 or n == 2:
        return b
    else:
        for i in range(3, n+1):
            a, b, c = b, c, a+b+c
        return c