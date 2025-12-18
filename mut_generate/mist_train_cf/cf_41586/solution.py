"""
QUESTION:
Implement a function called `calculate_factorial` that takes a single parameter `n` (0 <= n <= 12) and returns the factorial of `n`, which is the product of all positive integers less than or equal to `n`. The function should not use the `reduce` function or lambda functions.
"""

def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial