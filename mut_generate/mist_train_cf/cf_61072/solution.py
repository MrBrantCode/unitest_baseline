"""
QUESTION:
Develop an algorithm to generate the nth term of the Fibonacci sequence using iteration. The function should take a positive integer `n` as its parameter and return the corresponding term in the sequence. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two. The function should handle invalid inputs (non-positive integers) by printing an error message.
"""

def entrace(n):
    if n <= 0:
        print("Input should be a positive integer")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a = 0
        b = 1
        for i in range(2, n):
            fib = a + b
            a, b = b, fib
        return b