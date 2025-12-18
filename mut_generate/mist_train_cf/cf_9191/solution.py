"""
QUESTION:
Create a function named `fibonacci(n)` that calculates the nth Fibonacci number, where n is a positive integer. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. The function should return the nth number in this sequence.
"""

def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_list = [0, 1]  # Initializing the Fibonacci sequence
        for i in range(2, n):
            fib_list.append(fib_list[i - 1] + fib_list[i - 2])  # Calculating the next Fibonacci number
        return fib_list[-1]  # Returning the nth Fibonacci number