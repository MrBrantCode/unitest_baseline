"""
QUESTION:
Write a function named `factorial` that calculates the factorial of an integer `n` using an embedded loop with a time complexity of O(n) and a space complexity of O(1). The function should handle negative integers, returning "Invalid input" if the input is negative. The function should only use a single variable to store intermediate values during computation and should not use any built-in mathematical functions or operators.
"""

def entance(n):
    if n < 0:
        return "Invalid input"
    elif n == 0:
        return 1

    result = 1
    for i in range(1, abs(n) + 1):
        result *= i

    if n < 0 and n % 2 == 1:
        return -result
    else:
        return result