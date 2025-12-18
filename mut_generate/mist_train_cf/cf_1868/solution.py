"""
QUESTION:
Create a function `binomial_coefficient(n, r)` to calculate the binomial coefficient for two non-negative integers `n` and `r`, where `n` is greater than or equal to `r`. The function should return the binomial coefficient as an integer.
"""

def binomial_coefficient(n, r):
    def factorial(num):
        result = 1
        for i in range(1, num+1):
            result *= i
        return result
    
    return factorial(n) // (factorial(r) * factorial(n-r))