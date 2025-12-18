"""
QUESTION:
Write a function named `gen_fib` that generates a Fibonacci series up to a given number `n` and validates whether the generated sequence is indeed a Fibonacci sequence. The function should return the Fibonacci series if it's valid, otherwise it should return an error message. Note that a Fibonacci series is a sequence where each number (after the first two) is the sum of the two preceding ones, beginning with 0 and 1. The input `n` is a positive integer, and it is assumed to be at least 2.
"""

def gen_fib(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2]) 

    for i in range(2, len(fib)):
        if fib[i] != fib[i-1] + fib[i-2]:
            return "This is not a Fibonacci sequence."
    
    return fib