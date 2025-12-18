"""
QUESTION:
Create a function called fibonacci(n) that generates and returns the Fibonacci series as a list, starting from the initial term of 1 and 1, up to the n-th term. The function should handle positive integer values of n. It should also be efficient for large values of n and handle edge cases such as n <= 2. The function should return an error message if n is not a positive integer.
"""

def fibonacci(n):
    if n <= 0:
        return "Input is not a positive integer."
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        fib_list = [1, 1]
        for i in range(2, n):
            fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list