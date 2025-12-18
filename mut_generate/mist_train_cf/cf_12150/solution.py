"""
QUESTION:
Write a function `factorial(n)` to calculate the factorial of a given non-negative integer `n` without using the built-in factorial function. The function should use a loop instead of recursion and ensure that the loop iterates a maximum of 100 times.
"""

def factorial(n):
    if n == 0:
        return 1

    result = 1
    for i in range(1, n+1):
        result *= i

        # Exit the loop if the maximum iteration limit is reached
        if i >= 100:
            break

    return result