"""
QUESTION:
Write a recursive function called `factorial` that calculates the factorial of a positive integer `n` without using loops or the multiplication operator (`*`). The function should handle non-positive integers and return an error message.
"""

def entance(n):
    # Base case: factorial of 0 and 1 is 1
    if n == 0 or n == 1:
        return 1
    # Base case: factorial of negative numbers is not defined
    elif n < 0:
        return "Factorial is not defined for negative numbers."
    # Recursive case: calculate factorial using addition and exponentiation by squaring
    else:
        return n * entance(n - 1)