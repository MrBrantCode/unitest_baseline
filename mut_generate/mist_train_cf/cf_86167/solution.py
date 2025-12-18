"""
QUESTION:
Create a function called `is_fibonacci(n)` that takes an integer `n` as input and returns `True` if `n` is a Fibonacci number and `False` otherwise. Using this function, write a program that takes six integers as input, checks each number to determine if it is a Fibonacci number, and prints the result for each number. If any Fibonacci numbers are found, the program should also print the maximum Fibonacci number among them. Assume that the input values are always integers.
"""

def is_fibonacci(n):
    x = 0
    y = 1
    while y < n:
        z = x + y
        x = y
        y = z

    return n == y or n == 0