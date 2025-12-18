"""
QUESTION:
Create a function named `factorial(n)` that calculates the factorial of a given integer `n`. The function should return an error message if the input `n` is not an integer or if it's a negative number. The function should be able to handle edge cases.
"""

def factorial(n):
    # check if n is integer
    if not isinstance(n, int):
        return "Error: Input is not an integer."
    # check if n is negative
    if n < 0:
        return "Error: Input is a negative number."
    # calculate factorial 
    fact = 1
    for i in range(1, n+1): 
        fact = fact * i
    return fact