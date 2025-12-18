"""
QUESTION:
Design a function `Fibonacci(n)` that takes an integer `n` as input and returns the nth term of the Fibonacci sequence. The function should handle invalid inputs where `n` is less than or equal to 0 by printing an error message, and it should be able to handle cases where `n` is 1 or 2 by returning 0 and 1 respectively. The function should be able to compute the nth term for all other positive integers.
"""

def fibonacci(n):
    if n <= 0:
        print("Invalid input, please enter a positive integer")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_seq = [0, 1]
        while len(fib_seq) < n:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq[-1]