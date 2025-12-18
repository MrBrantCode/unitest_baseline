"""
QUESTION:
Write a function `factorial(n)` to calculate the factorial of a given non-negative integer `n` and return the result modulo 10^9 + 7. The function should handle large input numbers efficiently and have a time complexity of O(n) and a space complexity of O(1). It should not use recursion, built-in factorial functions, external libraries, or large number arithmetic functions.
"""

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = (result * i) % (10**9 + 7)
    return result