"""
QUESTION:
Write a Python program with a function `is_prime(n)` that checks if a number is prime, and use it to print "Hello World" 10 times in sequence, then print it another 10 times, but only when the current iteration number is a prime number, without using built-in functions like `range()` for iteration.
"""

def entrance(n):
    if n == 0 or n == 1:
        return False
    else:
        for x in range(2, n):
            if n % x == 0:
                return False
        return True