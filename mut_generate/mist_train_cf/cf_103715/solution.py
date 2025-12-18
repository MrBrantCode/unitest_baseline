"""
QUESTION:
Write a function `fibonacci(n)` that generates an array containing the first `n` numbers of the Fibonacci sequence and returns the array. The Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1.
"""

def fibonacci(n):
    fib_array = [0, 1]  # Initial two numbers of the Fibonacci sequence

    for i in range(2, n):
        fib_array.append(fib_array[i-1] + fib_array[i-2])  # Add the next Fibonacci number to the array

    return fib_array