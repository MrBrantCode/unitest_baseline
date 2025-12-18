"""
QUESTION:
Implement a recursive function `factorial(n)` to calculate the factorial of a positive integer `n` while keeping track of the number of function calls made. The function should have a time complexity of O(n), not use any loops or iteration, and handle edge cases such as large input values, returning an error message when necessary. Use memoization to improve the performance of the recursive function.
"""

def factorial(n, factorial_cache = {}):
    # Check if the input is valid
    if not isinstance(n, int) or n < 0:
        return "Error: Invalid input. Please provide a positive integer."

    # Base case: factorial of 0 is 1
    if n == 0:
        return 1

    # Check if the factorial value is already in the cache
    if n in factorial_cache:
        return factorial_cache[n]

    # Calculate the factorial recursively
    result = n * factorial(n - 1, factorial_cache)

    # Store the factorial value in the cache
    factorial_cache[n] = result

    return result