"""
QUESTION:
Implement a function named `factorial(n)` that calculates the factorial of a given non-negative integer `n` using a loop. The function should handle the following cases: 
- If `n` is negative, print an error message and return without a value.
- If `n` is zero, return 1.
- If `n` is a positive integer, return the computed factorial result.
"""

def entance(n):
    if n < 0:
        print("Error: Cannot compute factorial of a negative number")
        return
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n+1):
            result *= i
        return result