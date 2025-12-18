"""
QUESTION:
Calculate the factorial of a non-negative integer "n" (n ≤ 12) without using recursion or the math library's factorial function. Implement a function named "factorial" that takes an integer "n" as input and returns the product of all positive integers less than or equal to "n".
"""

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result