"""
QUESTION:
Create a program with two functions, `factorial_while_loop(n)` and `factorial_recursion(n)`, that calculate the factorial of a given integer `n`. The functions should handle non-integer and negative inputs by returning an error message. The `factorial_while_loop(n)` function must use a while loop, while the `factorial_recursion(n)` function must use recursion. The base case for recursion is when `n` is 0, in which case the function should return 1.
"""

def factorial_while_loop(n):
    if not isinstance(n, int):
        return "Error: Invalid input. Please enter a valid integer."
    elif n < 0:
        return "Error: Factorial is undefined for negative numbers."
    else:
        result = 1
        while n > 0:
            result *= n
            n -= 1
        return result

def factorial_recursion(n):
    if not isinstance(n, int):
        return "Error: Invalid input. Please enter a valid integer."
    elif n < 0:
        return "Error: Factorial is undefined for negative numbers."
    elif n == 0:
        return 1
    else:
        return n * factorial_recursion(n - 1)