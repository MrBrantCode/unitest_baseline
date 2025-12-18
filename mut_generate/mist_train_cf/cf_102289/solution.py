"""
QUESTION:
Write a function `factorial` that calculates the factorial of a given non-negative integer `n` using a loop. The loop should only iterate `n` times, or a maximum of 1000 times if `n` exceeds 1000. The function should use a single variable for calculation, without any intermediate variables, and return the result.
"""

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer n using a loop.

    The loop only iterates n times, or a maximum of 1000 times if n exceeds 1000.
    The function uses a single variable for calculation, without any intermediate variables.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of n, or "Factorial exceeds 1000" if the result exceeds 1000.
    """
    result = 1
    for i in range(1, min(n, 1000) + 1):
        result *= i
        if result > 1000:
            return "Factorial exceeds 1000"
    return result