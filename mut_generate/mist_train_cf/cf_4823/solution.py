"""
QUESTION:
Create a function `factorial(n)` that calculates the factorial of a given number `n`. The function should be optimized to handle large numbers with a time complexity of O(n). It should also include error handling to check if the input is a positive integer and return an error message if it is not. Additionally, the function should handle cases where `n` is close to the system's recursion limit by switching to an iterative approach to avoid potential stack overflow issues.
"""

def entance(n):
    # Error handling for non-positive integers
    if not isinstance(n, int) or n <= 0:
        return "Error: Input must be a positive integer"
    
    # Base case
    if n == 1:
        return 1
    
    # Recursive case
    if n > sys.getrecursionlimit() / 2:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    else:
        return n * entance(n - 1)