"""
QUESTION:
Create a function `add_and_factorial(x, y)` that takes two integers `x` and `y` as input, calculates their sum, and then returns the factorial of the resultant sum. The function should return "Factorial not defined for negative numbers." when the sum is negative, and 1 when the sum is zero.
"""

# Calculate factorial
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial

# Add two integers and calculate factorial
def add_and_factorial(x, y):
    sum_result = x + y
    return factorial(sum_result)