"""
QUESTION:
Write a function called `factorial` that calculates the factorial of a given number using recursion. The function should validate the input to ensure it is a non-negative integer. If the input is not a non-negative integer, return an error message.
"""

def factorial(n):
    # check if n is a float and if it is whole
    if isinstance(n, float) and n.is_integer():
        n = int(n)
    # Check if input is a non-negative integer
    if not isinstance(n, int) or n < 0:
        return "Error: Input must be a non-negative integer"
    # Base case: 0! = 1
    elif n == 0:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n-1)