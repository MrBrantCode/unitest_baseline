"""
QUESTION:
Create a function `binomial_coefficient(n, r)` that calculates the binomial coefficient for two non-negative integers `n` and `r`, where `n` is greater than or equal to `r`. The function should return the binomial coefficient as an integer.
"""

def binomial_coefficient(n, r):
    # Calculate the factorial of a number
    def factorial(num):
        if num == 0:
            return 1
        else:
            return num * factorial(num - 1)
    
    # Calculate the binomial coefficient
    return factorial(n) // (factorial(r) * factorial(n - r))