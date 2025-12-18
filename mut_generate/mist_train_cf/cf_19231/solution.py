"""
QUESTION:
Write a function `get_result(n)` that calculates the sum of all Fibonacci numbers up to the nth number, modulo 10^9 + 7. The function should use dynamic programming to generate Fibonacci numbers and return the sum of the first n numbers in the sequence, modulo 10^9 + 7.
"""

def get_result(n):
    fib = [0, 1] 
    for i in range(2, n):
        fib.append(fib[i-2] + fib[i-1]) 
    return sum(fib) % (10**9 + 7)