"""
QUESTION:
Create a recursive function named `factorial` that takes an integer `n` as input and calculates its factorial. The function should have a base case to prevent infinite recursion and should use recursive calls with modified arguments to calculate the factorial.
"""

def factorial(n):
    if n == 0:  # base case: factorial of 0 is 1
        return 1
    else:
        return n * factorial(n - 1)  # recursive call with a smaller argument