"""
QUESTION:
Create two functions, `fib_seq(n)` and `check_fib(fib)`. The `fib_seq(n)` function should generate a list of Fibonacci numbers from 1 to the nth term, where n is a positive integer. The `check_fib(fib)` function should take a list of Fibonacci numbers and return True if the sequence is accurate, and False otherwise. The functions should handle potential edge cases for the input.
"""

def fib_seq(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib

def check_fib(fib):
    n = len(fib)
    if n == 0:
        return True
    elif n == 1 and fib[0] == 0:
        return True
    elif n == 2 and fib == [0, 1]:
        return True
    else:
        for i in range(2, n):
            if fib[i] != fib[i-1] + fib[i-2]:
                return False
        return True