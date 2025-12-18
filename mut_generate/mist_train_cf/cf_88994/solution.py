"""
QUESTION:
Implement a recursive function `factorial(n)` that calculates the factorial of a positive integer `n` while keeping track of the number of function calls made. The function should have a time complexity of O(n), not use any loops or iteration, and handle edge cases such as large input values, returning an error message when necessary. Additionally, implement memoization to improve the performance of the recursive function.
"""

# Dictionary to store previously calculated factorial values
factorial_cache = {0: 1}

def factorial(n):
    # Check if the input is valid
    if not isinstance(n, int) or n < 0:
        return "Error: Invalid input. Please provide a positive integer."

    # Check if the factorial value is already in the cache
    if n not in factorial_cache:
        factorial_cache[n] = n * factorial(n - 1)

    return factorial_cache[n]