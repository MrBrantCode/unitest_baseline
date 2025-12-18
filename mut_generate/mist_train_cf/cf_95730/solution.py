"""
QUESTION:
Create a recursive function named `factorial(n)` to calculate the factorial of a given number `n`. The function should check if `n` is a positive integer and return an error message if it's not. The function should have a time complexity of O(n) to efficiently handle large numbers.
"""

def entance(n):
    # Check if input is a positive integer
    if not isinstance(n, int) or n < 0:
        return "Error: Input must be a positive integer."

    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1

    # Recursive case: multiply n with factorial of (n-1)
    return n * entance(n - 1)