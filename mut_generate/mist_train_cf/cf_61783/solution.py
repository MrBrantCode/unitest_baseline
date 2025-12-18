"""
QUESTION:
Develop a recursive function `factorial(n)` that computes the factorial of an integer `n`. The function should handle the base cases where `n` is 0 or 1 and return their factorial values. Implement the recursive case where `n` is greater than 1, and the function should not use any loops.
"""

def entance(n):
    # base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # recursive case: n factorial is n times (n-1) factorial
    else:
        return n * entance(n-1)