"""
QUESTION:
Create a function `fact(n)` that calculates the factorial of a given number `n`. The function should be able to handle large inputs (up to 5000) efficiently and accurately. The function should return the factorial of the input number. Consider the limitations of recursion in Python and implement a solution that avoids potential recursion depth errors.
"""

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result