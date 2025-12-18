"""
QUESTION:
Write a recursive function named 'factorial' that takes an integer 'n' as input and calculates its factorial. The function should be able to handle the base cases (n = 0 or 1) and use recursion for other cases.
"""

def factorial(n):
    # Base case: if n is 0 or 1, the factorial is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n factorial is n times (n-1) factorial
    else:
        return n * factorial(n-1)